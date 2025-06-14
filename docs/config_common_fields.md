# Config Common Fields

95% of what you need to know to use Augmentoolkit effectively is what the arguments in the config files mean.

Most configs contain many of the same arguments. This section gets you up to speed on those common, shared arguments.

## Common Section: `api`

Almost all pipelines have an `api` section. However most **compositions** (pipelines made of pipelines) have an API section *per pipeline* that they use. This allows for finer control but it it may mean that you don't see this section exactly as shown here in some of the more common things you may use, such as `complete_factual_datagen`.

```
api:
  small_api_key: !!PLACEHOLDER!! # deep
  large_api_key: !!PLACEHOLDER!!  # deep
  small_base_url: https://api.deepinfra.com/v1/openai
  large_base_url: https://api.deepinfra.com/v1/openai # http://localhost:2242/v1
  small_model: Qwen/QwQ-32B-Preview
  large_model: meta-llama/Meta-Llama-3.1-70B-Instruct
  small_mode: api
  large_mode: api
```

..._api_key is the API key for a model used in a pipeline. ..._base_url determines what provider you're going to use. ..._model determines what specific model you're going to ask that provider for. ..._mode is there in case you want to use a non-OpenAI-compatible API such as Cohere.

The most common layout of this field is to have a large and small model as you see above, though some pipelines have only one model (pdf cleaning).

The [Pipeline-Specific README]() will tell you whether a field should be a reasoning model or not. This varies by pipeline and by field. Most pipelines do not rely on reasoning models, though many steps support reasoning models by having their postprocessors strip out the think tags.

Field-by-field for the above example:
- `large_model` the name of the large model you want to use. This is the model that will be used for the final generation step, as well as question generation and revision. This should be a decently-strong model. Any field with "large_" coming before it in the `config.yaml` file configures this model: what provider you're using for it, what API key you're using for that provider, etc... this lets you use two different providers during the same dataset generation run.
- `large_api_key` this is where you put the API key for the API provider of the large and powerful model that you are using. If you're running a local server, put a dummy value in here so that the formatting of the request does not break.
- `large_base_url` this is the base URL for the API provider you are using. The large_base_url in particular configures the base URL for requests made to the large model. Some possible values:
    - http://localhost:2242/v1 <- aphrodite (local)
    - http://localhost:8080/ <- llama.cpp
    - http://localhost:11434/v1 <- Ollama
    - https://api.together.xyz <- together.ai, which offers quality open-source models for cheap prices. Their service has reliability issues sometimes, however.
    - https://api.groq.com/openai/v1 <- Groq. They offer their API for free but have low rate limits.
    - https://api.openai.com/v1/ # <- OpenAI
    - anything else that accepts OAI-style requests, so basically any API out there (openrouter, fireworks, etc...)
    - **You can see a lot of potential base_urls in the `config_overrides/` folder in the `original` pipeline.**
- `large_mode` is the mode that the pipeline will run in when making requests to the large model. `api` is the default mode, and is used for running the pipeline with APIs supporting the OpenAI standard. `cohere` is also supported, and is used for running the pipeline with the Cohere API (base_url does nothing in `cohere` mode). Other modes may be added in `augmentoolkit/generation_functions/engine_wrapper_class`.
- Anything with `small_` in the name is like its `large_` equivalent, but for the smaller model that handles more "bulk" tasks in the Pipeline like validation and initial chunk filtering.

## Common Section: `path`

`path` is where the input, output, and prompt folders are pointed at.

```
path:
  default_prompts: ./prompts
  input_dir: ./inputs/meta_scale
  output_dir: ./outputs/hidden_output_factual_test_lagattempt
  prompts: ./prompt_overrides/standard_set/prompts_override_open-ended_questions
```

Field-by-field:
- `input` the relative path to the folder where the raw text input is stored. This is the folder that contains the text files that you want to use as input to the pipeline. The files can be .txt and/or .md (.pdf and .docx coming soon). They can be nested inside folders if you want, so very little cleanup work is required when working with a new source of data that you might have lying around.
- `output` the relative path to the folder where the output of the pipeline will be stored. This is the folder that will contain the dataset files (.jsonl) that are generated by the pipeline, as well as a complementary continued-pretraining dataset. Intermediate generations (useful for debugging or interpretability) are also here.
- `default_prompts` the relative path to the folder where the core prompts of Augmentoolkit are stored. This is the folder that contains the prompt files that are used throughout the pipeline. `default_prompts` is the fallback folder that Augmentoolkit will use if it can't find a prompt in the `prompts` folder.
- `prompts` the relative path to the folder where the prompts for the current run of Augmentoolkit are stored. Compared to `default_prompts`, `prompts` is essentially an override: if a prompt is found in the `prompts` folder, it will be used instead of the prompt of the same name in the `default_prompts` folder. This allows you to create different prompts for new kinds of input data that the original prompts may not be well-suited for.


## Common Section: `system`

`system` is where the miscellaneous settings of a pipeline go. Of all the common sections, this one is the one that most commonly has additional, custom fields per pipeline. Still, some common settings are almost always present here:

```
system:
  completion_mode: False
  concurrency_limit: 300
  use_stop: True
  subset_size: 30
  use_subset: True # you will probably want to have use_subset on during testing and development to save money.
  chunk_size: 4000
```

- `CHUNK_SIZE` is an integer, the maximum number of characters to use in each "chunk" of text that will be fed through the pipeline. LLMs have finite context window so most documents fed into an Augmentoolkit pipeline need to be broken up into "chunks" of text. This parameter determines how big those chunks are allowed to be. Reduce this if you are getting API errors because your requests are exceeding the max context length of a model.
- `COMPLETION_MODE` *Completion Mode Should be Left False for Most Pipelines.* This is a boolean that determines whether prompts are sent to the provider in chat mode (default, what happens when it's set to `false`) or completion mode (what happens when it's set to `true`). Completion mode can produce higher-quality responses with some models, but many providers don't support it. The difference with completion mode vs chat mode is that completion mode basically has the LLM autocomplete a document, whereas chat mode involves a back-and-forth conversation. Completions can be useful for making the LLM's writing quality better for instance. But no Augmentoolkit pipeline is optimized for it and this is mostly a legacy/use-it-if-you-want-to-add-it-yourself option.
- `CONCURRENCY_LIMIT` is an integer; it's the maximum number of concurrent requests that can be made to the provider. This is useful for controlling costs, stopping timeouts, and preventing rate-limiting. Alternatively, if you have high rate limits, note that dataset generation is VERY parallelizable -- so increasing this can *multiply* your generation speed.
- `SUBSET_SIZE` controls the number of chunks fed through the pipeline if USE_SUBSET is on. This is useful for debugging and testing quickly and cheaply — only the first `SUBSET_SIZE` chunks will be processed. This is also very useful for workloads where you don't *need* to generate data from the whole input set -- factual SFT data is a good example of this, the model only needs to see so many conversations to "get the idea" so you can set subset size to a couple thousand and avoid generating an obscene amount of dataset.
- `USE_SUBSET` is a boolean that determines whether the pipeline uses a subset of the input data. See option above for information.

## Common Section: `cost`

`cost` is used in pipelines that have been configured with a "cost estimator" engine wrapper output observer. Basically, a little function attaches itself to the thing that makes all your LLM API calls, and tracks how many tokens you've sent to your model, and how many you've gotten back as output. Using what it tracks with these numbers you provide, you can estimate roughly how expensive per million input tokens *the pipeline is overall*.

A useful application of this might be to get an estimate of how roughly expensive a pipeline is using a small subset test run, and then extrapolating that to get an estimate of the overall cost.

```
cost:
    cost_per_million_small_input: 0.54
    cost_per_million_small_output: 2.18
    cost_per_million_large_input: 0.54
    cost_per_million_large_output: 2.18
```

Simply put the cost in USD per million tokens next to the large/small input/output field. All should be floats.

## Common Section: `meta_datagen`

`meta_datagen` configures whether or not a model saves its intermediate outputs in a trainable format. This is only useful if you want to train a model to *run that pipeline*. Most of the time you will want to disable this as it means that your output files will be significantly larger.
```
meta_datagen:
  do_meta_datagen: True
  meta_datagen_keys: # note that we will likely NOT have the original question generation detail -- or maybe we do.... hmm how do we... how do we use the full output of that but with the repaired context? Simple we do not. Hmm. HMM. do both and just use a different prompt and out format for the repaired-from-the-start thing? Oh and that's another one the pipeline will want to be able to change the output format of each thing to arbitrary variations nad also add random rules to the thing like "all caps" and other random shit just to make it really good at instruction following. Thankfully we have the inputs and outputs so we can twist it nicely. The output format, maybe we want to include a regex or some code or some way of parsing it so that we can then convert it to something else. A thought for when I go all into the model making stage.
    - clean_pdf_details
  meta_datagen_extras:
```

- `do_meta_datagen` boolean. Enable or disable meta datagen.
- `meta_datagen_keys` list of strings. The keys whose intermediate outputs you want to turn into trainable data.
- `meta_datagen_extras` a list of paths to prompts with {curly bracket interpolation, just like normal prompt files}. At the end of pipeline execution, these prompts will be filled in with keys from the final dict to produce custom trainable data. This is useful if you want to skip intermediate steps and train a model to produce the end result directly from an input, for instance by having a prompt that only makes use of the input text and final output keys.

#### Is something still on your mind?

If you have any open questions, feel free to head over to the [Discord](https://discord.gg/s6PBfsaVzu) and ask them! Alternatively, if you want to read tips that are useful in the areas of dataset generation and model training (but are not strictly necessary for Augmentoolkit's use, hence why they're not just on the README) you can check out this [free informal blog]((https://promptingweekly.substack.com/)) I post to.