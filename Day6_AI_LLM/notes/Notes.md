1. ARTIFICIAL INTELLIGENCE (AI)
Definition

AI is the branch of computer science focused on building machines/systems that can perform tasks that normally require human intelligence — reasoning, learning, perception, language understanding, planning, and decision-making.

Brief History
1950: Alan Turing proposes the "Turing Test" as a measure of machine intelligence.
1956: Term "Artificial Intelligence" coined at the Dartmouth Conference.
1950s–1980s: Symbolic AI / rule-based expert systems dominate (e.g., MYCIN for medical diagnosis).
1990s–2000s: Statistical ML methods gain ground (SVMs, decision trees).
2012 onward: Deep learning breakthrough (AlexNet wins ImageNet) triggers the modern AI boom.
2022 onward: Generative AI (ChatGPT and similar) brings AI into mainstream daily use.

Types of AI (by capability)
Narrow AI (Weak AI) — designed for one specific task (e.g., spam detection, voice assistants). All AI in use today is narrow AI.
General AI (Strong AI / AGI) — hypothetical AI with human-level intelligence across all domains. Does not exist yet.
Super AI — hypothetical AI surpassing human intelligence. Purely theoretical.
Types of AI (by approach)
Symbolic/Rule-based AI: uses hand-crafted logic rules (if-then). Predictable but brittle; can't handle ambiguity well.
Machine Learning-based AI: learns rules/patterns from data. Flexible, scales with data, but needs training data and compute.

Branches of AI
Machine Learning
Natural Language Processing (NLP)
Computer Vision
Robotics
Expert Systems
Speech Recognition
Planning & Search algorithms


Advantages
Automates repetitive/complex tasks
Processes huge amounts of data faster than humans
Improves accuracy in prediction-heavy domains
Available 24/7, no fatigue
Limitations
Can be a "black box" (hard to explain decisions, especially DL)
Requires quality data; biased data → biased outcomes
High computational/energy cost at scale
Lacks true understanding/common sense reasoning


2. MACHINE LEARNING (ML)
Definition

ML is a subset of AI where systems learn patterns directly from data and improve their performance on a task without being explicitly programmed with rules for every scenario.

How it works (core loop)
Collect data → 2. Choose a model/algorithm → 3. Train (model adjusts internal parameters to reduce error on training data) → 4. Validate/test on unseen data → 5. Deploy → 6. Monitor and retrain.
Types of ML

a) Supervised Learning — learns from labeled data (input–output pairs).

Regression (predicts continuous values): Linear Regression, Polynomial Regression → e.g., predicting house prices.
Classification (predicts categories): Logistic Regression, Decision Trees, Random Forest, SVM, k-NN → e.g., spam vs not-spam.

b) Unsupervised Learning — learns structure from unlabeled data.

Clustering: K-Means, Hierarchical Clustering, DBSCAN → e.g., customer segmentation.
Dimensionality Reduction: PCA, t-SNE → e.g., compressing features while preserving structure.
Association: Apriori algorithm → e.g., market basket analysis ("customers who bought X also bought Y").

c) Semi-supervised Learning — uses a small amount of labeled data + a large amount of unlabeled data.

d) Reinforcement Learning (RL) — an agent learns via trial and error by interacting with an environment, receiving rewards or penalties.

Key terms: agent, environment, state, action, reward, policy.

Examples: game-playing AI (AlphaGo), robotics, RLHF (used to align LLMs).
Key Concepts
Features: input variables used to make predictions.
Labels: the correct output the model tries to predict (supervised learning).
Training vs Test set: data split to train the model and then evaluate it on unseen data.
Overfitting: model memorizes training data but performs poorly on new data.
Underfitting: model is too simple to capture patterns in the data.
Bias-Variance tradeoff: balancing a model that's too simple (high bias) vs too sensitive to training data (high variance).
Evaluation metrics: Accuracy, Precision, Recall, F1-score (classification); MSE, RMSE, MAE (regression).
Advantages
Learns and improves automatically from experience/data
Handles complex patterns humans might miss
Works well for structured/tabular data even with less compute than DL
Limitations
Needs substantial labeled data (for supervised learning)
Requires manual feature engineering in many classical algorithms
Performance plateaus on very complex/unstructured data (images, raw text) compared to DL


3. DEEP LEARNING (DL)
Definition

DL is a subset of ML that uses artificial neural networks with many layers ("deep") to automatically learn hierarchical representations of data — removing the need for manual feature engineering.

Neural Network Basics
Neuron: computes a weighted sum of inputs, adds a bias, passes through an activation function.
Activation functions: ReLU, Sigmoid, Tanh, Softmax — introduce non-linearity so the network can learn complex patterns.
Layers: Input layer → Hidden layers (the "deep" part) → Output layer.
Forward propagation: data flows through the network to produce an output.
Backpropagation: the network calculates the error and propagates it backward, adjusting weights to reduce error (using gradient descent).
Loss function: measures how wrong the model's prediction is (e.g., cross-entropy, MSE).
Optimizer: algorithm that updates weights to minimize loss (e.g., SGD, Adam).

Key Architectures
CNN (Convolutional Neural Network): specialized for grid-like data (images); uses filters/kernels to detect edges, textures, shapes, objects. Used in image classification, object detection, medical imaging.
RNN/LSTM/GRU (Recurrent architectures): designed for sequential data (text, time series, speech) by maintaining a "memory" of previous inputs. Mostly superseded by Transformers for language tasks now.
Transformer: uses a self-attention mechanism to process entire sequences in parallel and capture long-range relationships. The foundation of virtually all modern LLMs (GPT, Claude, Gemini, etc.) and also used in vision (Vision Transformers).
GAN (Generative Adversarial Network): two networks (generator + discriminator) compete — generator creates fake data, discriminator tries to detect fakes, improving both over time. Used for image generation, deepfakes, art.
Autoencoders/VAEs: compress data into a smaller representation and reconstruct it; used for anomaly detection, denoising, generative tasks.
Why Deep Learning Excels
Automatically learns features from raw data (pixels, raw text) — no manual feature engineering needed.
Scales well with more data and compute — performance keeps improving (unlike many classical ML algorithms that plateau).
State-of-the-art on unstructured data: images, audio, video, natural language.
Advantages
Extremely high accuracy on complex/unstructured data
Eliminates manual feature engineering
Scales with data — more data + more compute generally = better performance
Limitations
Requires massive datasets and compute (GPUs/TPUs)
Long training times, high energy cost
"Black box" — difficult to interpret why it made a decision
Prone to overfitting without proper regularization


4. GENERATIVE AI (GenAI)
Definition

GenAI is a subset of Deep Learning focused on models that generate new, original content (text, images, audio, video, code) rather than just classifying or predicting a fixed label.

How it Differs from Traditional AI/ML/DL
Traditional models are discriminative — given an input, predict a label/category/number (e.g., "is this email spam?").
Generative models are generative — given a prompt or noise, produce new content that resembles the patterns in training data (e.g., "write an email," "draw a cat").
Core Techniques Behind GenAI
Transformers (Large Language Models): generate text token-by-token by predicting the most likely next token given context — powers GPT, Claude, Gemini, LLaMA, DeepSeek.
Diffusion Models: start with random noise and iteratively "denoise" it into a coherent image guided by a text prompt — powers Midjourney, Stable Diffusion, DALL-E.
GANs: generator vs discriminator competition, historically used for image generation before diffusion models became dominant.
VAEs (Variational Autoencoders): learn a compressed latent space of data and sample from it to generate new variations.
Categories of Generative AI
Text generation: ChatGPT, Claude, Gemini — writing, summarizing, coding, Q&A.
Image generation: DALL-E, Midjourney, Stable Diffusion.
Audio/Music generation: Suno, ElevenLabs (voice cloning/synthesis).
Video generation: Sora, Runway.
Code generation: GitHub Copilot, Claude Code, Cursor.
Training Pipeline (for LLMs specifically)
Pretraining: model learns general language patterns by predicting the next token across massive internet-scale text.
Fine-tuning: model is further trained on curated/instruction data to follow directions properly.
RLHF / preference tuning: human feedback (or AI feedback, as in Constitutional AI) shapes the model to produce helpful, safe, and aligned responses.
Advantages
Massively boosts productivity in content creation, coding, research
Can personalize/adapt output to a given prompt or style
Lowers the barrier to producing professional-quality text, images, code
Limitations
Hallucination: can generate plausible-sounding but false information
High compute/training cost
Copyright and originality concerns around training data
Can be misused (deepfakes, misinformation, phishing content)
Output quality depends heavily on prompt quality


5. HOW THEY RELATE (Hierarchy)
Artificial Intelligence (AI)
        │
        └── Machine Learning (ML)
                    │
                    └── Deep Learning (DL)
                                │
                                └── Generative AI (GenAI)

Each is a subset of the one before it:

All ML is AI, but not all AI is ML (rule-based systems are AI but not ML).
All DL is ML, but not all ML is DL (a decision tree is ML but not DL).
All GenAI (as commonly used today) is built on DL, but not all DL is generative (a CNN classifying images is DL but not generative).