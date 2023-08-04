<!--

author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0.0
current_version_description: Initial version
module_type: standard
docs_version: 1.3.0
language: en
narrator: US English Female
mode: Textbook

title: Demystifying Large Language Models

comment:  Learn about large language models (LLM) like ChatGPT.

long_description: There's lots of talk these days about large language models in academia, research, and medical circles.  What is a large language model, what can it actually do, and how might LLMs impact your career?  Learn more here!

estimated_time_in_minutes: 60

@pre_reqs
None.  
@end

@learning_objectives  
After completion of this module, learners will be able to:

- Define "large language model" (LLM) 
- Give a brief description of n-grams and word vectors
- Give a brief description of a neural network
- Give one example of a task that an LLM could do that could advance a biomedical project or career
- Give one example of a caveat or pitfall to be aware of when using an LLM

@end

@version_history 
 No previous versions.
@end

good_first_module: false 
@sets_you_up_for

@end

@depends_on_knowledge_available_in

@end 

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->

# Demystifying Large Language Models

@overview

## Large Language Models: Definitions

Large language models (LLMs) like [ChatGPT](https://openai.com/chatgpt) (and other [GPT models](https://openai.com/product) developed by OpenAI) or [BERT](https://arxiv.org/abs/1810.04805) are getting a lot of attention these days.

We can build a basic understanding of what an LLM is based upon the three words in its name. LLMs are: 

* **Large**. Very large, in fact, with billions of parameters created from complex numerical representations of words, sentences, paragraphs and grammar (known as "vectors").
* **Language** related.  They take language as input and give language as output. 
* **Models**.  They attempt to predict, or model, desired behavior.  In this case that means they try to generate what would be a likely result in the real world if real people generated the text output for the given input.

LLMs can generate language (human language and even computer language) that appears to be written by human intelligence.  In fact, we can even ask LLMs which are employed as conversational agents (chatbots) to explain themselves, and the resulting text is well-composed and realistic.  That's what we'll try on the next page!

### What Do They Say About Themselves?

When given the prompt, "briefly explain, in three to five sentences, what a large language model is and how it can be used in biomedical research," this is what [ChatGPT](https://openai.com/chatgpt) offered:

> A large language model, such as GPT-3, is an advanced artificial intelligence model designed to understand and generate human-like text based on the patterns it learns from vast amounts of training data. In biomedical research, these models can be used to analyze and generate text related to medical literature, clinical trials, patient records, and scientific articles. They can assist researchers in tasks such as information extraction, summarization, literature review, and even generating hypotheses by synthesizing existing knowledge. By leveraging their language processing capabilities, large language models can accelerate research, improve data analysis, and aid in decision-making processes in the biomedical field.

We'd disagree with some of the AI-generated explanation of large language models you just read.  For example, the use of the word "understand" seems to indicate cognition and subjectivity, which artificial intelligence lacks. Additionally, the use of the word "learns" can be misleading.  


[Bing AI Chatbot](https://chat.bing.com) replied (and included footnotes!):

> Large language models (LLMs) such as GPT-3 have the potential to revolutionize biomedical research by helping scientists quickly and accurately analyze vast amounts of data. One of the most promising applications is in natural language processing (NLP) of biomedical literature. LLMs can efficiently navigate through the scientific literature, assisting researchers in literature reviews and information synthesis^1^. They can also be used to understand biomedical text^2^.<br/><br/>Learn more: 1. blog.bionl.ai 2. labs.feinberg.northwestern.edu 3. link.springer.com

Here, we again have concerns about the use of the word "understand", and we'd put an asterisk beside the word "accurately."

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

**In this module, we will always disclose when we're using an LLM to generate text**.  
<br/><br/>
The use of LLMs to generate text in science and education is a controversial issue. Some proponents of these tools point out that using LLMs can help equalize access to language.  For example, LLMs can provide sample language to people who need to write an abstract or proposal in a language that they lack native fluency in.  Others indicate that LLMs can speed up routine tasks that require just a quick review of accuracy, like summarizing a manuscript for a lit review. However, there are also critics who believe that using LLMs to generate text is a form of plagiarism or even scientific misconduct.
<br/><br/>
We're not here to advocate for a particular stance in the ethical disputes around LLMs, but we do think that it's only fair to let you know when the text you're reading has been generated by a sophisticated model.

</div>

While these definitions are helpful, there are some changes we will propose, especially in terms of "learning", "understanding", and "accuracy."  Our human-created definition is on the next page.

### A Human Definition

Can large language models "learn" and "understand"?  Not in the way humans do!

"Learning" for LLMs (at least for now) means consuming enormous amounts of text and discovering how words interact with each other.  It's a study of mathematical probability and patterns, not meaning.  

Consider, for example, that a human (you, for example) can analyze geometric patterns and make good guesses as to what should appear next in a sequence, without attributing meaning to those symbols.  You could, with practice and some systems of tracking what you've seen so far, be able to predict what symbol would make sense in a pattern and what would be out of place.  Similarly, large language models can analyze the complex symbolic system of human language and make very good predictions of a realistic pattern, without any cognition or true understanding.

As seen on the previous page, ChatGPT and Bing AI were able to imitate, thanks to their exposure to many types of text, the kinds of words and patterns that appear in descriptions of technology. They also were able to predict what kinds of words are associated with the phrase "biomedical researchers".  These systems aren't mulling over meaning, however, they are pattern matching.  The importance of this distinction is crucial. **These powerful tools are not modeling reality or truth, they are modeling language**.  

A Human-Generated Definition 
------

Given what we've discussed so far, we'd propose a definition for biomedical researchers that is a bit more humble:

Large language models are predictive systems that, after having analyzed huge volumes of text, are able to generate realistic texts that closely mimic human language.  They excel at imitating the form of language, that is, patterns of words and grammar, punctuation, word difficulty, and text length, all without having conceptual understanding of the meaning of the language they are generating.  Because of their accurate depiction of the form of human language, LLMs are useful for generating sample texts that may or may not be truthful.  Researchers may choose to use these tools to accelerate language tasks like literature reviews and abstract generation, but should disclose their use of these tools and be careful when it comes to trusting the accuracy of LLM-generated text. 

## How Do LLMs Work?

We know what an LLM is -- a system that mimics human language.  But how did these LLMs come to be?  How did they become so good at imitating language, to the degree that they almost seem to have understanding and cognition?  To understand how LLMs came to be, we'll start by introducing just a bit of natural language processing (NLP).  We'll then move into neural networks and deep learning. 

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

The next two pages may feel a bit dense.  If you don't need to know the history of large language models, you can just skim these pages. 
<br/><br/>
We'll add a **"TL;DR"** ("too long, didn't read") summary to the top of each page so you can get the main points.
<br/><br/>

</div>

### Natural Language Processing

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>
As promised, here's the TL;DR of this page:

* **N-grams** are strings consisting of n words. "Happy Birthday to you, Happy" is a 5-gram, for instance.
* Being exposed to lots of n-grams in language is useful for predicting an upcoming word (e.g. "Birthday").
* Words can be represented as vectors which are located in n-dimensional space in which each word has a numeric value for each dimension.
* Advances in language modeling required the use of neural networks.

</div>

A **natural language** is a language used to communicate by humans among themselves, like English or Swahili or Cantonese.  **Natural language processing** or NLP is the computerized analysis of natural language.  NLP includes tasks of trivial complexity, such as calculating word frequency in documents, as well as complex tasks such as predictive text generation.  NLP is a type of computing that falls under the large umbrella of "artificial intelligence", or AI.

In this module we'll talk only about **language models**, which are systems build to predict or generate text.  We won't address the many other areas of NLP which can be interesting to biomedical researchers, such as **named entity recognition** (for example, looking through clinical notes to find mentions of symptoms or illnesses that belong to an ontology such as SNOMED), **part of speech tagging** (e.g., measuring pronomial underuse in the language generated by autistic subjects), **sentiment analysis** (e.g., predicting depression risk related to patients' writings), etc. 

Heuristic Models
------

Early language models were **heuristic**, or rules-based systems. For example, [ELIZA](https://dl.acm.org/doi/10.1145/365153.365168), an early model of therapeutic language, had a rule on how to respond to texts that lacked keywords that would ordinarily be used to guide the automated reply. "Please go on" was one potential response to such a situation.

N-grams
-----

Later, language models relied on statistical probability, and aimed to predict the next word given a string of previous words, an **n-gram**. The letter **n** here, as in many places, is a number. A bigram, for example, is a sequence of two words, and a trigram a sequence of three words.  Larger numbers of words in a sequence are usually called by the number: 5-grams, 10-grams, and generically as n-grams.  N-grams prove very useful in language prediction, because the probability of selecting the next word in a series goes up as the number of lead-in words goes up.

For example, can you predict the next word of a text if the preceding word is "and"?  It's very unlikely you'd guess correctly.  What about the word following "and they"?  You might guess (correctly) that the next word is a verb or part of a verb phrase, but which one? "And they are," "and they will," "and they thought," etc. are all reasonable guesses.  

What if we provided the text, "and they lived happily"? If you've been exposed to English since childhood, you might be able to guess (correctly) that the next word is "ever", and that this is part of the common ending of children's stories in English: "and they lived happily ever after."

Vectorizing Models
---

Another way of predicting language relies on thinking of words as **vectors**.  Vectorization  (also called **word embedding**) models are sophisticated systems that rely on neural networks, a topic we'll explore on the next page.

Imagine a 3D space with three axes.  A vector consists of an arrow beginning at the origin, the intersection of the axes, and ending at a specific point in three-dimensional space.  Vectors can be similar, because they end at points that are close together and the angle formed between the two vectors is small.  Or they can be very different because they are opposite one another, with a large angle between them. 

In the image below (thanks to [academo's 3D Vector Plotter](https://academo.org/demos/3d-vector-plotter/)), there are two vectors that are quite similar, the red and the blue vectors.  The orange vector appears to be orthogonal to the others and is therefore less similar.

![A three-dimensional coordinate system with three vectors.  All originate at a common point, and the red and blue continue to points that are close to one another.  The orange vector goes in a direction that appears to be a right angle to the other vectors.](media/vectors.png)

Words can be thought of as being vectors occupying n-dimensional space. These dimensions aren't attributes we could quickly summarize like "animal relatedness", or "degree of pleasant connotation" but consist of aspects of language that are modeled computationally based on analyzing words that appear in similar contexts or are related in some way in training text. 

For example, in our image of the three vectors above, maybe the blue vector is the word "insect", the red vector is the word "bug", and the orange is the word "elevator".  In reality, these vectors would be in a highly dimensional space, with the number of dimensions much greater than three!

Words are modeled as multidimensional mathematical objects, which in turn enables language models to go beyond statistically predicting output text based on n-gram frequency.  Words have features that can be measured and have math performed on them, and this allows for prediction that includes an understanding of the distance or similarity between words.

At this point in language modeling, researchers now have to rely on sophisticated systems called **neural networks** to model words as vectors.  Let's talk about those systems next.

### Neural networks

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>
As promised, here's the TL;DR of this page:

* **Neural networks** are systems that use lots of small calculations using **weights** that interact with one another to result in a final prediction.  A neural network (also known as a **deep learning** model) consists of an input layer which transmits input values to a hidden layer (or more than one) which analyzes inputs, and an output layer which collates results.
* **Transformers** revolutionized language neural networks because they allowed more efficient access to context clues from further back in text than other systems allowed.  Today's LLMs rely on transformers.

</div>

Trial and Error
---

To understand neural networks, it's important to know that in machine learning (whether that's in a neural network or in another type of algorithm), there's a lot of trial and error.  In machine learning, the speed of calculation that a computer can offer allows the computer to try thousands of different values for the coefficient of a predictor variable, for example.  This allows the computer to determine which value ends up being the best coefficient, and do that for many different predictor (input) variables.

![A figure with a hat states, "Oh, hey, you organized our photo archive!".  A second figure replies, "Yeah, I trained a neural net to sort the unlabeled photos into categories."  The first figure resonds, "Whoa! Nice work!."  The caption below the drawing reads: "Engineering tip: When you do a task by hand, you can technically say you trained a neural net to do it."](https://imgs.xkcd.com/comics/trained_a_neural_net.png "[Trained a Neural Net](https://xkcd.com/2173/) comic by xkcd, [CC BY-NC 2.5](https://xkcd.com/license.html).")<!-- style = "max-width: 220px;" -->Neural networks take this power of trial and error and massively expand it. Neural networks are an attempt to in some way replicate the operations of neurons in a brain. Various nodes (neurons) receive input, perform some mathematical transformation on that input, and either "fire" (pass some output on to a next step) or not, depending on whether the result of the calculation passes a certain threshold.  Each node starts off with random weights that determine how to mathematically transform the data it receives, and the computer tries many combinations of weights to see which ones are the most accurate. 


An Example
-----

Let's consider a binary question.  Will a given person buy takeout for dinner?  Given seven input variables, you want a single outcome: 1 for "yes, they will get takeout" and 0 for "no, they will not get takeout."

In this image (created thanks to [NN-SVG](http://alexlenail.me/NN-SVG/index.html)), the leftmost column of circles represent **inputs**.  Maybe one input is an individual's level of tiredness, another is the number of days they have had takeout in the last week, a third input could be the number of leftovers in the person's fridge.  These inputs are scaled and normalized.

![A depiction of a neural net, which consists of three columns of circles, the first of which has seven circles and is the input layer, the second of which has ten circles and is the hidden layer, and the last of which has one circle and is the output layer.  Lines connect the circles from the first column to circles in the second column, and circles in the second column to the circle in the third column.](media/example_nn.png)Lines of various intensity show the **weights** (think of them like coefficients in an equation) that each of these inputs contribute to ten nodes in the **hidden layer**, which is a set of nodes between input and output. The darker the line, the heavier that input is weighted for that node's calculation. Some nodes might heavily consider one's previous takeout habits, for example, while others disregard it entirely. Each hidden layer node calculates the sum of all its weighted inputs, and each one comes up with its own unique answer.<br/><br/>
Then, each node in the hidden layer either fires (sends output) to the next layer, which is our output layer, or it doesn't (for example, one node in the hidden layer doesn't reach a threshold of activation, so it doesn't fire).  The output layer also uses weights to calculate how much each hidden layer node contributes to its calculation.  Then a sum is calculated, and the final prediction is made: "yes, they will order takeout," or "no, they will not."

This prediction is checked for accuracy on a set of labeled data (data on 500 people who either got takeout or did not).  Then, the weights are changed, and **that** set of weights is evaluated for accuracy.  Over time, after much repetition, the weights reach a point in which additional small changes don't improve performance any more, and the final set of weights is set.  Now we have a model that we can use for prediction.

The model depicted above has only one hidden layer between input and output, but there can be an arbitrary number of hidden layers.  We can think of the number of hidden layers in a neural network as its "depth".  As neural networks gained more and more layers, the term **deep learning** emerged to describe these increasingly complex models.

Transformers
---

The way we think about language as humans doesn't just rely on the last few words we heard or read.  We don't have a simple four, five, or 100 word buffer or sliding window that we use to predict language.  We keep in mind the theme of the conversation or the literary genre we're reading or the overall reading level of a text.  We remember that the text is a novel, a political speech, a child's review of a movie, or a religious song.  We hold context clues in mind, even long after these clues appeared. This can be referred to as "attention." 

The ability for language models to maintain attention to relatively distant context clues was necessary for language models to become more human-like.  After a few different attempts to make neural networks able to "look back" at prior context (such as recurrent neural networks or RNNs), a new, more efficient method to keep distant clues salient to prediction was developed.  This new algorithm was called a [transformer](https://arxiv.org/pdf/1706.03762.pdf), and from 2017 forward, the use of transformers changed language models. Language models became efficient enough to allow for many more parameters and became truly large.  There's some dispute about what could be called the first true LLM, but contenders include ELMo (Embeddings from Language Model) from 2017, GPT-1 (Generative Pre-trained Transformers-1) from 2018, and BERT (Bidirectional Encoder Representations from Transformers), also released in 2018.

## LLM Costs and Risks

Costs
---

Over time, with advances in the speed and size of computer processors (especially Graphical Processing Units, or GPUs), faster and more efficient data storage, and competition among cloud providers, computing has become less expensive.  That means that tasks can be performed today that would have been unrealistic (in terms of time and expense) to perform a few years ago.  That's true across computing, and it's certainly true in artificial intelligence.  But "less expensive" doesn't mean free.  Large language models are incredibly resource intensive, in terms of the amount of input required, the amount of computing required, and the energy consumed in building and running the models. 


Risks
---

Additionally, there are important risks to consider.  We're going to borrow a framework from Weidinger et al.  In their superb and approachable ["Ethical and social risks of harm from Language Models,"](https://arxiv.org/abs/2112.04359) Weidinger and her co-authors enumerate six domains of risks, harms, and costs associated with large language models.  We summarize these risks below (and note, we have avoided the temptation to ask a large language model to summarize the text for us):

1. Discrimination, exclusion, and toxicity
-----

Where can one obtain huge amounts of text, generated by humans, for free?  The internet!  Language models and their abilities to predict text have grown in part because of better, faster, and cheaper computers, but also in part because of the massive proliferation of human-generated text that can be analyzed.  Unfortunately, this set of language is biased in terms of who generates it and the opinions they share.  Toxic language, stereotypes, and bias abound, and these have already been documented in text generated by LLMs.  

2. Information Hazards
------

Information hazards can be thought of as the flip-side of misinformation harms (discussed later on this page). That is, an information hazard can cause harm via the sharing of _true_ information. 
Because the training data given to LLMs is so vast, there are cases of private information such as home addresses being leaked by LLMs.  Additionally, LLMs might correctly infer and disclose sensitive information while amassing and summarizing data (for example, accurately disclosing a serious disease diagnosis to an unprepared user asking about their symptoms).

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

Because many LLM chatbots ([including ChatGPT](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)) save user inputs and use them to further refine their models, it is possible that information that **you submit** in a chat could create a future information hazard via an information leakage incident. For this reason, you should **never supply private information in a chat prompt**, including personally identifying information, information about human research participants, PHI, proprietary secrets, and more. 

</div>

3. Misinformation Harms
---

As we stated earlier, LLMs are language models.  They are not intended to model truth, science, or the universe, but rather, to generate language that realistically mimics the language it was trained on. The data that LLMs are trained on includes jokes, sarcasm, disinformation, opinion, deception, mistakes that are later corrected, and other uses of language that do not transmit true information in the way an LLM user might be hoping for.  

Misinformation is particularly pernicious when language is realistic in its form and tone, but includes false information.  In early 2023, a lawyer used ChatGPT to prepare a filing only to discover that [the LLM had cited non-existent case law](https://www.forbes.com/sites/mollybohannon/2023/06/08/lawyer-used-chatgpt-in-court-and-cited-fake-cases-a-judge-is-considering-sanctions/?sh=57d3675a7c7f). 

In fact, the risk of completely fabricated information that has little to no truth is so well established that this phenomenon has a name -- **hallucinations**.  LLMs are said to hallucinate when they generate objectively false text.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Misinformation risks for science and medicine are non-trivial.  Imagine using an LLM to create a methods section or literature review that turns out to be demonstrably false.  Worse still, imagine automating letters to patients about their radiology or lab results and sending erroneous suggestions that put their health in danger!

</div>

4. Malicious Uses
---

While we hope that biomedical researchers would never intentionally misuse technology, it is important to highlight that language is a powerful tool in the hands of malicious users.  LLMs can empower bad actors with convincing language that could be used for social engineering (convincing humans to click a link in an email, for example) or disinformation campaigns.  LLMs could also be used to condense information about political dissidents, for example, to make the role of a surveilling authority more efficient.  Finally, since LLMs can generate computer code, it may become much easier for unskilled bad actors to write malicious code.

5. Human-Computer Interaction Harms
---

Many of us already use digital assistants like Siri or Alexa.  These digital assistants tend to be depicted in female ways, which some argue promotes stereotypes about the role of women in society as subordinate helpers.  This kind of harm could potentially be amplified with widespread use of conversational LLMs.  Additionally, because the language generated by these systems is so convincing, users might overestimate the reliability of LLMs, thinking of them as though they were intelligent interlocutors with the ability to reason, empathize, and act morally.  Unmerited trust could lead to a user's unsafe reliance on a large language model as well as their unsafe sharing of private information to a "friendly" and "trustworthy" conversational agent.

6. Automation, Access, and Environmental Harms
---

LLMs require significant energy (with its associated carbon burden) as well as other resources, such as water for data center cooling needs and materials for computer chips.  The extraction and use of these resources can harm the environment and directly and indirectly harm people.  People are also potentially harmed by other aspects of LLMs, including employment related risks as jobs are automated or made less creative by the use of LLMs.  Artists and authors, for example, are already contending with threats to their livelihood and the use of their works as training data.  Finally, there is a risk of widening the digital divide and exacerbating differences in access to the benefits of technology.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

![A figure with a ponytail indicates some words projected onto a screen while saying "An analysis of our new AI hiring algorithm has raised some concerns."  On the screen is displayed "DeepAIHire Candidate Evaluation Algorithm, Inferred Internal Weightings.  What follows is a table of weights that each apply to various factors.  There are four tiny weights and one enormous weight.  They are: weight 0.0096 for the factor of Educational Background, weight 0.520 for the factor of Past Experience, 0.0208 for Recommendations, 0.0105 for Interview Performance and a huge 783.5629 for the factor described as "Enthusiasm for developing and expanding the use of the DeepAIHire Algorithm."](https://imgs.xkcd.com/comics/ai_hiring_algorithm_2x.png "[AI Hiring Algorithm](https://xkcd.com/2237/) comic by xkcd, [CC BY-NC 2.5](https://xkcd.com/license.html).")<!-- style = "max-width: 280px;" -->This risk framework reflects a point in time, and you may think of risk types or examples that aren't reflected here. Suffice it to say, LLMs, like any laboratory tool, must be used with discretion and an awareness of the risks, costs, tradeoffs, and utility they provide.

</div>

## Benefits of LLMs

Any process that uses language can potentially benefit from LLM technology.  Consider some of these use cases, which we supplement with examples of prompts we supplied and replies we received from ChatGPT.  We've shortened the LLM-generated text and have added ellipses (...) to show where we've trimmed text in order to make this a quicker read.

Structure and Scaffolding
---

Use LLM's to create an outline for a manuscript, slide deck, CV, or other highly structured literary genre, given a topic.  This is an example of relying on what an LLM excels at (form) without undue reliance on what might fail (factual scientific content).

Prompt: **"Make an outline for a peer-reviewed manuscript describing a clinical trial."**

> I. Title:<br/>
>    A descriptive title summarizing the main objective of the clinical trial.<br/>
> <br/>
> II. Abstract:<br/>
>    A concise summary of the study, including the background, objectives, methods, results, and conclusion.<br/>
> <br/>
> III. Introduction:<br/>
>    A brief introduction to the research problem, highlighting the significance and rationale for conducting the clinical trial.<br/>
> <br/>
> ...
> <br/>
> XII. References:<br/>
>    A comprehensive list of cited references following a specified citation style (e.g., APA, AMA).<br/>
> <br/>
> XIII. Appendices:<br/>
>    - Additional information, such as study protocols, informed consent forms, or supplementary tables/figures.<br/>
>    - Detailed description of any statistical methods used.<br/>
> <br/>
> Note: The actual content and structure of the manuscript will depend on the specific details of the clinical trial, research area, and journal guidelines.<br/>

Summarizing 
-----

Use LLMs to summarize texts, advance literature reviews, or get to key themes.

Prompt: **"Summarize the main points of Strubell's 'Energy and Policy Considerations for Deep Learning in NLP'."**

> "Energy and Policy Considerations for Deep Learning in NLP" is a research paper written by Emma Strubell that explores the environmental impact and policy implications of deep learning in Natural Language Processing (NLP). Here are the main points of Strubell's paper:
> 
>  ...
> 
> Overall, Strubell's paper raises awareness about the energy consumption and environmental impact of deep learning in NLP. It highlights the need for energy-efficient approaches, policy interventions, and collective responsibility to address the energy challenges associated with large-scale NLP models.

Draft text for use in research settings
---

Handle this use case with care.  With careful disclosure and accuracy checking, biomedical researchers may wish to use LLMs to create first drafts of certain texts.

Prompt: **"Write a brief letter of recommendation for my research assistant Mary Saetang, who did a great job with human subjects in autism research."** 

> [Your Name]<br/>
> [Your Position/Title]<br/>
> [Your Institution/Organization]<br/>
> [City, State, ZIP Code]<br/>
> [Email Address]<br/>
> [Date]<br/>
> <br/>
> [Recipient's Name]<br/>
> [Recipient's Position/Title]<br/>
> [Recipient's Institution/Organization]<br/>
> [City, State, ZIP Code]<br/>
> <br/>
> Dear [Recipient's Name],<br/>
> <br/>
> I am writing to highly recommend Mary Saetang for her outstanding work as a research assistant in our autism research project, particularly in the area of human subjects. Mary has been an invaluable member of our team, demonstrating exceptional skills, dedication, and professionalism throughout her time with us.<br/>
> <br/>
> ...
> <br/>
> Should you require any further information or have any questions, please do not hesitate to contact me. Thank you for considering Mary Saetang for this opportunity.<br/>
> <br/>
> Sincerely,<br/>
> <br/>
> [Your Name]<br/>
> [Your Position/Title]<br/>
> [Your Institution/Organization]<br/>

Working With Code 
---

Again, this is an area in which users should exercise particular care.  Do not inadvertently disclose data, statistical descriptions of your data, findings, database schema or other potentially sensitive information.

Prompt: **"Using tidyverse R code, write code that will take a dataframe column called 'id' and break it into two columns called 'subject\_id' and 'accession\_number'.  The data in the 'id' column has these two values stuck together with an underscore between them."**

> Certainly! Here's an example of how you can use the tidyverse package in R to split the 'id' column into 'subject\_id' and 'accession\_number' columns based on the underscore delimiter:<br/><br/>
> <div  style="background:black; color:white;"><pre>
library(tidyverse)<br/>
<br/>
# Assuming your dataframe is named 'df'<br/><br/>
df <- df %>%<br/>
           separate(col = id, <br/>
                    into = c("subject\_id", "accession\_number"), <br/>
                    sep = "_", <br/>
                    remove = FALSE)<br/>
<br/>
# Printing the updated dataframe<br/>
print(df)<br/>
</pre></div><br/>
> In this code, we first load the tidyverse package using `library(tidyverse)`. Then, we use the `%>%` operator from the magrittr package to perform a series of operations on the dataframe 'df'.<br/>
> ...
> <br/>
> After running this code, the 'id' column will be split into 'subject\_id' and 'accession\_number', with the values separated by underscores.<br/>

Translate texts
----

Consider your institution's policies with regard to translation and whether regulation would impede your use of AI translation.  Translations should be considered draft texts that should be verified by professionals.

Prompt: 

**Translate the sentence, "You will be compensated for your time with a gift card worth $10 each time you appear at your scheduled laboratory visit and complete an EEG" to Spanish** 

> Será compensado por su tiempo con una tarjeta de regalo por valor de $10 cada vez que aparezca en su visita programada al laboratorio y complete un EEG.

**Translate the sentence, "You will be compensated for your time with a gift card worth $10 each time you appear at your scheduled laboratory visit and complete an EEG" to Kreyol**

> W'ap resevwa yon konpansasyon pou tan ou ak yon kadò pou $10 chak fwa ou parèt nan vizit laboratwa ou ki planifye epi ou konplete yon EEG.

-----

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

These are powerful examples, and you may generate many more in your investigation of the utility of LLMs. Keep in mind that anything you generate using an LLM has **no guarantee of accuracy** and that you have a responsibility to validate the correctness of AI-generated output.

Also, be aware that the use of LLMs to contribute language to manuscripts is expressly forbidden by many major publications and may result in unpleasant career consequences.

</div>

## Quiz

Large language models respond best to well crafted input texts, or prompts.  Consider this prompt, which we gave to ChatGPT: 

Prompt: **"Create a quiz question about n-grams."**

> Question: What is an n-gram in natural language processing?<br/><br/>
>A) A single word or character in a text.<br/>
>B) A sequence of n words or characters in a text.<br/>
>C) A statistical measure of word frequency in a text.<br/>
>D) A technique to analyze the grammatical structure of a sentence.<br/><br/>
>Please select the correct option (A, B, C, or D).

That's too easy!  Here's a better one, created by ChatGPT in response to the prompt **"Create a multiple choice quiz question about n-grams and how they are used in predicting language."**  Please do try and answer it!

------

**Which of the following statements best describes n-grams and their role in predicting language?**

[( )] N-grams are numerical values assigned to words in a language, used to predict their frequencies in a given text.
[(X)] N-grams are sets of adjacent words or characters in a text, used to analyze patterns and predict the likelihood of specific words or phrases.
[( )] N-grams are complex algorithms used to predict the syntax and grammatical structure of sentences in a language.
[( )] N-grams are specialized dictionaries used in natural language processing to identify and categorize words based on their semantic meanings.
***
<div class = "answer">

**This explanation of the answer was created by a human, not by ChatGPT.**

N-grams aren't numerical values, algorithms, or dictionaries. The correct answer is that n-grams are sets of adjacent words or characters (in fact, n consecutive words), used to analyze patterns and predict the likelihood of specific words or phrases.  

</div>
***

-------

When prompted, **"Create a multiple choice quiz question that tests a learner's understanding of what a large language model is."**, ChatGPT gave us the following:

-----

Question: What is a large language model?

[[ ]] A tool used for translating languages on the internet.
[[ ]] A type of supercomputer used for complex data analysis.
[[ ]] A neural network-based AI model capable of understanding and generating human-like text.
[[ ]] A specialized software used by linguists to study ancient languages.
***
<div class = "answer">

**This explanation of the answer was created by a human, not by ChatGPT.**

A large language model does deal with language, but it's not (at least not primarily or exclusively) a tool used for translating language on the internet.  LLMs are models, not computers or software, so "a type of supercomputer..." is incorrect, as is "a specialized software...."  The correct answer is that a large language model is a neural network-based AI model capable of understanding and generating human-like text.  Keep in mind that the word "understanding" here does not refer to cognitive or subjective understanding, but functional predictive abilities.

</div>
***

-------


When prompted, **"Create a multiple choice question with several correct answers that asks 'which of the following are true statements about large language models'"**, ChatGPT gave us the following:

-----

**Which of the following are true statements about large language models? (Select all that apply.)**

[[X]] A) Large language models are trained on vast amounts of text data.
[[X]] B) They utilize deep learning techniques, such as neural networks.
[[X]] C) These models can generate coherent and contextually relevant text.
[[ ]] D) They require minimal computational resources for training and inference.
[[ ]] E) Large language models have the ability to understand and interpret human emotions.
[[X]] F) They have been instrumental in advancing various natural language processing tasks.
***
<div class = "answer">

This time, we asked ChatGPT to explain the answers.  We added emphasis like **bold** text: 

>Here's a brief explanation for each statement:
>
>**A) Large language models are trained on vast amounts of text data.**
>This statement is **true** because large language models require substantial amounts of text data to train effectively. The models learn from billions of sentences or documents to capture the diverse patterns and structures of language.
>
>**B) They utilize deep learning techniques, such as neural networks.**
>This statement is **true** because large language models typically employ deep learning techniques, particularly neural networks. Neural networks are powerful models that can learn complex representations of language and are commonly used in training large language models.
>
>**C) These models can generate coherent and contextually relevant text.**
>This statement is **true** because large language models have demonstrated the ability to generate text that is coherent and contextually relevant to a given prompt. They analyze the input context and use the patterns learned during training to produce text that follows grammar rules and makes sense in the given context.
>
>**D) They require minimal computational resources for training and inference.**
>This statement is **false**. Large language models, such as GPT-3, actually require substantial computational resources for both training and inference. Training such models involves processing huge amounts of data and performing multiple iterations of training, which demands significant computational power. Similarly, generating text or performing inference with large language models is computationally intensive.
>
>**E) Large language models have the ability to understand and interpret human emotions.**
>This statement is **false**. While large language models can generate text that appears to understand emotions to some extent, they lack true understanding and interpretation of human emotions. The models do not possess emotions themselves but instead learn statistical patterns from the training data to generate text that can evoke emotional responses.
>
>**F) They have been instrumental in advancing various natural language processing tasks.**
>This statement is **true**. Large language models have made substantial contributions to advancing natural language processing tasks. They have achieved state-of-the-art performance in various tasks such as machine translation, text summarization, sentiment analysis, question answering, and language generation. These models have significantly improved the capabilities of language understanding and generation systems.
>
>These explanations clarify why each statement is either true or false based on the characteristics and capabilities of large language models.


</div>
***

----

We asked **'Give a multiple choice quiz question about the hidden layer in neural networks which would be appropriate for beginners'.**, the Bing AI Chatbot gave us this:

-----

**What is the purpose of the hidden layer in a neural network?**

[( )] A. To provide input to the network 
[( )] B. To provide output from the network 
[(X)] C. To perform computations on the input data 
[( )] D. To store the output data
***
<div class = "answer">

**This explanation of the answer was created by a human, not by ChatGPT.**

(A) is incorrect because the **input layer** is what holds input values and forwards that data to the hidden layer.  Similarly, (B) and (D) incorrect, because the **output layer** stores and forwards output from the system to the requestor.  The correct answer is (C).  The hidden layer performs computations on input data.

</div>
***

----

We asked ChatGPT for a question on word vectorization.  Our prompt: **
Write a quiz question that checks for understanding of the term "vector" as it applies to word vectorization in NLP.**

---

In the context of word vectorization in Natural Language Processing (NLP), what does the term "vector" refer to?

[(X)] A) A mathematical representation of a word's meaning or context.
[( )] B) A machine learning algorithm used for text classification.
[( )] C) A type of neural network architecture commonly used in NLP.
[( )] D) A technique for preprocessing text data before analysis.
***
<div class = "answer">

**This explanation of the answer was created by a human, not by ChatGPT.**

Vectors are mathematical representations of various dimensions of a word, which allow for numerical calculations and comparisons to judge word similarity and work with words in a mathematical model.  The answer, then, is (A).

</div>
***

---

For our next question, we tried several different prompts in different LLMs before we were satisfied with the question.  We finally got a good question with this prompt: **'Create a quiz question with seven potential answers to the prompt, "Which of these are risks or costs associated with using a large language model".  Make at least two of the potential answers correct.'**

We disagree, however, with the answers to this quiz question, so we'll pose the question to you and explain what ChatGPT suggested the correct answers were and what we think the correct answers are!

------

**Which of these are risks or costs associated with using a large language model?**

[[X]] A) Increased computational resources and energy consumption.
[[X]] B) Potential biases and perpetuation of societal inequalities.
[[X]] C) Limited interpretability and transparency of model outputs.
[[X]] D) Higher risk of data breaches and security vulnerabilities.
[[X]] E) Reduced creativity and originality in generated content.
[[X]] F) Decreased accessibility for users with limited internet connectivity.
[[X]] G) Difficulty in adapting to new language patterns and emerging slang.
***
<div class = "answer">

This is what ChatGPT claims:

> Correct answers: <br/>
> A) Increased computational resources and energy consumption. <br/>
> B) Potential biases and perpetuation of societal inequalities. <br/>

We, however, see all of these as at least **potential** risks:

* LLMS require enormous energy and computational resources (A)
* LLMs are built on human language which reflect societal bias, and this will appear in their outputs (B)
* LLMs are built on complex deep learning models and it is hard to grasp how an LLM generated particular content (C)
* Because of the risks of anthroporphizing them and disclosing sensitive data when giving prompts, LLMs can introduce new data breach and security risks (D)
* Perhaps controversially, we believe that human writers are capable of novel uses of language that language models cannot fully mimic (E)
* It's possible that LLMs will exacerbate the digital divide, reduce employment for automatable jobs, and decrease access to technology for some (F)
* LLMs are often trained on a static dataset, which, unless it is constantly updated, represents a point in time that will not capture novel language use (G)

</div>
***

Finally, we're going to leave AI behind for one final question: 

**Think about your own research, and write out how a large language model could improve or accelerate your work, and where it could introduce risk.**

Clicking "submit" doesn't actually send this to us, and your answer isn't being evaluated in any way.

[[___ ___ ___]]

<details>

<summary>Click here to see our answer</summary>

<div class = "answer">

We don't know what your research entails, or what your intentions are for the use of AI in your career.  Maybe you'll use it to help scaffold code or handle some of your unpublished writing tasks, such as drafting emails.  However, regardless of your use of large language models, we encourage you to:

* Make no assumptions about the accuracy of any text generated by LLMs 
* Disclose your use of LLMs
* Investigate the policies of your institution, the journal you submit to, your granting agency, etc.
* Consider not only the massive benefits of LLMs but also the very real risks that come along with using them

</div>
</details>


## Additional Resources

LLMs:

* [ChatGPT (at the time of this module creation, built on GPT-3.5)](https://openai.com/chatgpt) 
* [GPT-4](https://openai.com/gpt-4)
* [Bing AI Chatbot (at the time of this module creation, built on GPT-4)](https://chat.bing.com)
* [BERT](https://cloud.google.com/ai-platform/training/docs/algorithms/bert-start)

Popular Press / Blogs:

* [Large language models: their history, capabilities and limitations](https://snorkel.ai/large-language-models-llms/) is an overview by the company Snorkel that is appropriate for people who aren't experts in the field.
* [An introduction to word embeddings for text analysis](https://www.shanelynn.ie/get-busy-with-word-embeddings-introduction/) builds intuition around words as vectors, with both common-sense explanations and great visualizations.
* [The Illustrated Word2vec](http://jalammar.github.io/illustrated-word2vec/) is a superb page that explains word vectorization with both simplicity and depth.  This is a long piece but worth reading and watching (there's an embedded YouTube video with the author walking you through the article), as it builds your intuition about the intersection of words and their mathematical representation.

Peer-reviewed literature:

* [Ethical and social risks of harm from Language Models](https://arxiv.org/abs/2112.04359): a superb overview of the risk landscape in LLMs
* [Attention is All You Need](https://arxiv.org/pdf/1706.03762.pdf): Google's work on Transformer models
* [Distributed Representations of Words and Phrases and their Compositionality](https://proceedings.neurips.cc/paper_files/paper/2013/file/9aa42b31882ec039965f3c4923ce901b-Paper.pdf)

History:

* [The manuscript describing ELIZA](https://dl.acm.org/doi/10.1145/365153.365168)

Other:

* [ChatGPT cites non-existent case law](https://www.forbes.com/sites/mollybohannon/2023/06/08/lawyer-used-chatgpt-in-court-and-cited-fake-cases-a-judge-is-considering-sanctions/?sh=57d3675a7c7f)
* [New ways to manage your data in ChatGPT](https://openai.com/blog/new-ways-to-manage-your-data-in-chatgpt).  OpenAI offers users a way to exempt their prompts from training data: "ChatGPT users can now turn off chat history, allowing you to choose which conversations can be used to train our models."

Publication Standards:

* [Editorial on AI and authorship policies](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10140602/)
* [Elsevier's take on AI in scientific writing](https://www.elsevier.com/about/policies/publishing-ethics#:~:text=The%20Use%20of%20Generative%20AI%20and%20AI%2Dassisted%20Technologies%20in%20Scientific%20Writing)
* [Nature's take on AI-generated content](https://www.nature.com/nature-portfolio/editorial-policies/ai)
* [Science's take on AI-generated text](https://www.science.org/content/page/science-journals-editorial-policies#:~:text=Artificial%20intelligence%20(AI)

## Feedback

@feedback
