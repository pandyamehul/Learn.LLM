# Learn AI - LLM

- [Learn AI - LLM](#learn-ai---llm)
  - [Week 1: Learn LLM, Explore Top models and Transformers](#week-1-learn-llm-explore-top-models-and-transformers)
  - [Week 2 : Build Multimodel chatbot - LLM, Gradio \& Agents](#week-2--build-multimodel-chatbot---llm-gradio--agents)
  - [Week 3 : Open Source Gen AI - Build Automated Solution with HuggingFace](#week-3--open-source-gen-ai---build-automated-solution-with-huggingface)
  - [Week 4 : LLM Exploration and Evaluation, Code generation and Business task](#week-4--llm-exploration-and-evaluation-code-generation-and-business-task)
  - [Week 5 : Retrieval-Augmented Generation (RAG)](#week-5--retrieval-augmented-generation-rag)
  - [Week 6 : Transitioning to Frontier Model Training \[4 Hr 20 min\]](#week-6--transitioning-to-frontier-model-training-4-hr-20-min)
  - [Week 7 : Advanced Training Techniques \[3 Hr 40 min\]](#week-7--advanced-training-techniques-3-hr-40-min)
  - [Week 8: Deployment and Finalization \[3 Hr 38 min\]](#week-8-deployment-and-finalization-3-hr-38-min)

## Week 1: Learn LLM, Explore Top models and Transformers

- Exercises and tasks related to LLMs, including API usage and model interactions.
- Includes notebooks for practical exercises and code snippets for working with LLMs.
- Environment setup for running LLMs locally or via APIs.
- Focus on understanding LLMs, their capabilities, and how to interact with them effectively.
- Includes examples of using OpenAI's API and Ollama for model interactions.
- Exercises include constructing API messages, handling responses, and streaming outputs from LLMs.

## Week 2 : Build Multimodel chatbot - LLM, Gradio & Agents

Day1:

- Exploration of Google Gemini, DeepSeek, and Anthropic's Claude models.
- Practical exercises using these models via their respective APIs.
- Includes examples of setting up system prompts, handling chat completions, and streaming responses.
- Example of conversation between different APIs, such as OpenAI and Google Gemini.

Day 2:

- Introduction to Gradio for building interactive UI applications with LLMs.
- Practical exercises on creating Gradio UI apps to interact with LLMs.

Day 3:

- Build chat bots using Gradio UI and OpenAI's API.
- Exercises on creating chat interfaces, handling user inputs, and displaying model responses.
- Implementation of context management for maintaining conversation history.

Day 4:

- Implemented AI Chatbot with integration of Ollama and OpenAI models.
- Intorcution and usage of tools in chatbot

Day 5:

- Multi-modal AI chatbots using OpenAI's DALL-E for image generation and speech models.
- Integrated audio generation using OpenAI's speech model.
- Exploration of agentic AI concepts, including breaking down complex tasks and using multiple LLMs for specialized tasks.
- Introduction to building multi-modal chatbots that can handle both voice and image inputs.
- Practical exercises on creating a multi-modal AI assistant for airline travel, integrating voice and image capabilities.
- Includes examples of using OpenAI's API for image generation and audio synthesis.

Additional End of week Exercise - week 2

```txt
- Now use everything you've learned from Week 2 to build a full prototype for the technical question/answerer you built in Week 1 Exercise.
- This should include a Gradio UI, streaming, use of the system prompt to add expertise, and the ability to switch between models. Bonus points if you can demonstrate use of a tool!
- If you feel bold, see if you can add audio input so you can talk to it, and have it respond with audio. ChatGPT or Claude can help you, or email me if you have questions.
- There are so many commercial applications for this, from a language tutor, to a company onboarding solution, to a companion AI to a course (like this one!).
```

**Challange to Explore:**

```txt
- Add more Tools / Agents to enhance capabilities: Add another Tool to make a booking
- Add an Agent that translates all responses to a different language and shows on the right hand side, using a different Frontier model
- Add an Agent that can listen for Audio and convert it to Text

What you can now do

- Describe transformers and explain key terminology
- Confidently code with the APIs for GPT, Claude and Gemini
- Build a multi-modal AI Assistant with UI, Tools, Agents
```

## Week 3 : Open Source Gen AI - Build Automated Solution with HuggingFace

Challange to Explore:

```txt
Generating Synthetic Data

- Write models that can generate datasets
- Use a variety of models and prompts for diverse outputs
- Create a Gradio UI for your product

What you can now do

- Confidently code with Frontier Models
- Build a multi-modal AI Assistant with Tools
- Build an LLM solution combining frontier and open-source models
```

## Week 4 : LLM Exploration and Evaluation, Code generation and Business task

Day 1, 2:

- Hugging Face Open LLM Leaderboard for comparing open source language models.
- Understand top 6 leader boards categories and their evaluation metrics viz. HuggingFace Open LLM, HuggingFace BigCode, HuggingFace LLM Perf, HuggingFace Others, Vellum, SEAL.
- Vellum.ai to compare open and close source models and performance.
- seal.com/leaderboard - another website to compare model performance.
- lmarena.ai/leaderboard - leaderboard to compare llm chatboats and their performance. ref. chatboat arena leaderboard.
- Harvy.ai
- Nebula.io - for resume and help manager to short list resume
- Bloop - legacy code conversion
- Saleforce.com
- Khanmigo.ai
- lmarena.ai
- scale.com/leaderboard/coding

Day 3:

- Created a C++ code generator using OpenAI's API.
- Integrated the code generator into a Gradio UI for interactive code generation.
- Added functionality to compile and run the generated C++ code within the Gradio interface.
- lmarena.ai/leaderboard - leaderboard to compare llm chatboats and their performance.

Day 4:

- Understanding of how open source models can be used and implemented to code generation task using HuggingFace inference endpoints.
- Deploy model on AWS or Azure or GCP for production use. Here, open source models will be installed on selected cloud compute, it provides end point to interact with deployed open source model.

Day 5:

- To be updated

**Challange to Explore:**

```txt
For this high performance coding solution

- Try adding Gemini to the Closed Source mix
- Try more open-source models such as CodeLlama and StarCoder, and see if you can get CodeGemma to work

3 new, exciting code generation ideas:

- A code tool that automatically adds docstring / comments
- A code gen tool that writes unit test cases
- A code generator that writes trading code to buy and sell equities in a simulated environment, based on a given API.

What you can now do

- Code with Frontier Models including AI Assistants with Tools, and with open-source models with HuggingFace transformers
- Confidently choose the right LLM for your project, backed by metrics
- Build solutions to generate code with Frontier and open-source LLMs
```

## Week 5 : Retrieval-Augmented Generation (RAG)

- Master RAG to improve the accuracy of your solutions.
- Become proficient with vector embeddings and explore vectors in popular open-source vector datastores.
- Build a full business solution similar to real products on the market today.

Day 1:

- Implemented simple, brute-force RAG (Retrieval-Augmented Generation) OpenAI's API.
- Integrated the RAG pipeline into a Gradio UI for interactive document retrieval and question answering.
- Added functionality to handle user messages and maintain chat history.
- Implemented a context-aware chat feature to improve response relevance.
- Added a function to enrich user messages with relevant context before sending them to the model.

Day 2:

- Implemented text chunking and embedding for document retrieval.
- Integrated text chunking into the RAG for improved context handling.
- Added a function to retrieve relevant document chunks based on user queries.

Day 3:

- Extended Day 2 activity
- Converted documents into embeddings for improved retrieval.
- Store chunk embeddings in a vector database for efficient similarity search using ChromaDB.
- Added 2D and 3D visualization of vector embeddings using TSNE.

Day 4-1:

- Implemented RAG pipeline with LangChain.
- Integrated document retrieval and response generation into a cohesive workflow.
- Added support for multi-turn conversations and context management.
- Integrated End to end flow using Gradio for user interaction.

Day 4-2:

- Implemented similar visualization techniques for the FAISS vector store.
- Created 2D and 3D scatter plots to visualize document embeddings stored in the FAISS index.
- Used t-SNE for dimensionality reduction and improved visualization clarity.

Day 5:

- Added debugging and troubleshooting steps for chromadb integration.

**Challange to Explore:**

```txt
Create a Knowledge Worker on your information to boost productivity

- Assemble all your files in 1 place; your personal Knowledge Base
- Vectorize everything in Chroma - your vector datastore
- Build a Conversational AI and ask questions!

Advanced ideas to take it to the next level

- If you use Google Workspace, use Google's API to read your own docs
- If you use MS Office, use libraries to read Office docs
- Harder - use libraries to connect to your email inbox, and Slack, and more!
```

## Week 6 : Transitioning to Frontier Model Training [4 Hr 20 min]

- Move from inference to training.
- Fine-tune a Frontier model to solve a real business problem.
- Build your own specialized model, marking a significant milestone in your AI journey.

Day 1:

- Fine tune LLM from inference to training, Finding and crafting the right dataset for fine tuning - sources and techniques. Data curation and preprocessing techiques for fine tuning. Optimizing training data - scrubbing, formatting, and augmenting data for better results. Evaluation of model centric vs. business centrics.

Day 2:

- Understand deployment pipeline for LLM and how to productionize applications.
- When to use prompting, RAG and fine tuning.
- Productionize LLM - best practices and strategies for deploying AI models at scale.
- Optimize large dataset for model training - data curation strategies. Create balanced dataset for training.
- Create and upload fine tuned dataset to HuggingFace.

Day 3:

- Understand and explore - Bag of words, Machine learning - baseline for NLP.
- Understanding of Traditional Machine Learning techniques such as - Feature engineering & linear regression, Bag of words, word2vec (Linear regression and Random forest and SVR)
- Baseline model in Machine Learning - implementation of simple prediction functions, feature engineering techniques for product price prediction models.
- Optimize LLM performance - advance feature engineering strategies, Linear regression for LLM fine tuning and base model comparison. Bag of words NLP, Implementing count vectorizatier for Text Analysis in ML.
- Support vector regression vs Random forest regression for price prediction - ML face-off. Comparision of Traditional Models from Random to Random Forest.

Day 4:

- Evaluating Frontier models (GPT-40-min, Claude-3.5-Sonnet) performance with baseline models.
- Implemented price prediction model - Human vs AI models.
- GPT-4-mini evaluation for price prediction / estimation task.
- Claude-3.5-Sonnet evaluation for price prediction / estimation task.
- Comparision of AI LLM Models output with traditional ML models for accuracy or prediction.

Day 5:

- Fine tuning LLM with Open AI- Preparing data, training and evaluating.
- Three stage approach to fine tune Open AI model viz.:-
  1. Preparing dataset in jsonl format for fine tuning - formatting and uploading to OpenAI.
  2. Run Training - training loss and validation loss should decrease.
  3. Evaluate result, tweak and repeat to fine tune model - using test dataset to evaluate model performance.
- Understanding - how to prepare JSONL files for fine tuning LLMs.
- Step by step understanding of launching GPS Fine tuning jobs on OpenAI API. Track training jobs, monitor progress and loss progress with weight and bias. Analyzing training and validation loss.
- Challange - When model performance doesn't improve and Best Practices for optimization of fine tuning LLMs.

## Week 7 : Advanced Training Techniques [3 Hr 40 min]

- Dive into advanced training techniques like QLoRA fine-tuning.
- Train an open-source model to outperform Frontier models for specific tasks.
- Tackle challenging projects that push your skills to the next level.

Day 1:

- Understand Parameters for efficient fine tuning - Low Rank Adaptation (LoRA), Quantized LoRA (QLoRA) & Hyperparameters.
- Understanding of LoRA adapter technique for efficient fine tuning of large language models.
- Understanding of QLoRA technique for fine tuning large language models with quantized weights.
- (Google Colab Session) Optimize LLM - R, Alpha and Target modules in QLoRA fine tuning., PEFT for LLMs with huggingface.
- Quantize LLM - Reduce model size with 8-bit precision, NF4 - advance technique for 4-bit LLM quantization, Explore PEFT model - role of LORA adapter in LLM fine tuning.

Day 2:

- How to choose best base model for fine tuning - Factors to consider, Model size vs performance trade-off, Domain-specific models.
- Which Model to choose? Depends on number of parameters, Llama vs Qwen vs Phi vs Gemma.
- Review model by analyzing HuggingFace leaderboard. [HuggingFace Leaderboard Open LLM](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
- (Google Colab Session) Exploration of Tokenizers for LLMs - LLAMA, QWEN and other LLM models. Tokenizing Llama 3.1 base model.
- (Google Colab Session) Optimize LLM Performance - loading and Tokenizing Llama 3.1 base model. Review quantization impact onn LLMs - analyze performance metrics and error.
- (Google Colab Session) validate tokenizer performance with 4 bit and 8 bit quantized LLMs.

Day 3:

- Fine tuning open source model using QLoRA - Step by step implementation.
- Understand the Hyperparameters used during training.
- 5 hyperparameter QLoRA
  - **Target Modules**: Train lower dimentioned metric and then apply to target module on selected layer in bigger model.
  - **R (Rank)**: Low rank matrix to approximate weight update.
  - **Alpha**: Scaling factor for weight update.
  - **Quantization Bits**: Number of bits for model weight quantization. reduce weight size and memory usage to train bigger models.
  - **Dropout**: Technique to prevent overfitting by randomly dropping units during training.
- Understanding of epochs, batch sizes, Learning rate, Gradient accumulation and optimizers.
- (Google Colab Session) setup open source LLM model training and fine tuning using QLoRA.

Day 4:

- (Google Colab Session) Understanding concept how we can train model keeping training cost low with high efficiency. (refer week 6 - day 2 light scenario)
- (Google Colab Session) apply effective fine tuning techniques to optimize training cost and performance using smaller datasets. for qlora fine tuning.
- Monitor the performance of fine tuning model and jobs on weights and biases.
- Advance techniques, tools on weights and biases and savings model on HuggingFace hub.
- Monitoring and managing training with weights and biases. Check model performance on weights and biases and also check model gets uploaded to hub repository.

Day 5:

- Understanding of 4 steps in LLM training from Forward pass to Optimization step.
  - **Forward Pass**: Input data is passed through the model to generate predictions. Predict the next token in training data.
  - **Loss Calculation**: The model's predictions are compared to the actual target values using a loss function to quantify the error.  How different was it to the true next token.
  - **Backward Pass**: Gradients of the loss with respect to the model's parameters are computed using backpropagation. how much should we tweak parameters to do better next time the gradients.
  - **Optimization Step**: The model's parameters are updated using an optimization algorithm (like Adam or SGD) to minimize the loss. Update model parameters using gradients to reduce loss.
- Understanding QLoRA training process - forward pass, backward pass and loss calculation.
- Understanding of softmax and cross-entropy loss function in LLM training.
- Analysis and monitoring of fine tuning llm models on weights and biases. Compare model performance over different execution. Evaulate fine tuned training model metrics on weights and biases.
- Visualize results - loss curves, accuracy metrics and more. Output would have better prediction.

## Week 8: Deployment and Finalization [3 Hr 38 min]

- Deploy your commercial product to production with a polished UI.
- Enhance capabilities using Agents.
- Deliver your first productionized, agentized, fine-tuned LLM model.
- Celebrate your mastery of AI and LLM engineering, ready for a new phase in your career.
