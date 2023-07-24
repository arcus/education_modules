<!--

author:   Joy Payton
email:    paytonk@chop.edu
version:  1.0.0
current_version_description: Initial version
module_type: standard
docs_version: 1.0.0
language: en
narrator: US English Female
mode: Textbook
previous_sequential_module: demystifying_regular_expressions

title: Regular Expressions Basics

comment:  Begin to use regular expressions, or regex, for simple pattern matching.

long_description: Regular expressions, or regex, are a way to specify patterns (such as the pattern that defines a valid email address, medical record number, or credit card number).  Learn to compose basic regular expressions in order to find and use important data.

estimated_time_in_minutes: 60

@pre_reqs
Learners should have some knowledge about patterns in biomedical data and understand the utility of regular expressions (regex).  For an introduction to these concepts, consider the [Demystifying Regular Expressions](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_regular_expressions/demystifying_regular_expressions.md#1) module. Having previously encountered an online regular expression checker may also be useful.
@end

@learning_objectives  
After completion of this module, learners will be able to:

- Define a simple alphanumeric pattern in regex notation
- List common ranges and character groups in regex
- Quantify characters appearing optionally, once, or multiple times in regex

@end

@version_history 
No previous versions.
@end
good_first_module: false
coding_required: true
coding_level: basic
sequence_name: regex
previous_sequential_module: demystifying_regular_expressions
@sets_you_up_for

@end 
@depends_on_knowledge_available_in
- demystifying_regular_expressions
@end
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->

# Regular Expressions Basics

@overview

## Regular Expression Refresher

As a reminder, the word *regular* (like *regulate*) comes from the Latin root for "rule": *regula*.  A **regular expression** (also known as "regex") is a specific way to **express** a **rule** for a pattern, such as "three or more upper case letters followed by exactly two digits, the first of which cannot be a 0, followed by a decimal point and two more digits."  Regular expressions can look like an odd combination of characters.  

By the end of this module you will be able to express this pattern as the regular expression `[A-Z]{3,}[1-9]\d\.\d{2}`.

Regular expressions are useful to biomedical researchers because they can allow you to find, replace, or extract text that matches patterns you define.  These text patterns might appear in your data (for example, clinical notes), in metadata (such as column names), in your data analysis scripts (for example, where you define hexadecimal codes for color), and in file names.  

A good place to practice regular expressions is an online regex testing website.  We like **Regex 101** at https://www.regex101.com, but you can also search online for "regex checker" to find other, similar websites.  Regex 101 allows you to enter your regular expression as well as some sample text that you want to apply the regular expression to.  You can use this website to gain practice with any of the rules you learn in this module.

The [Regex 101 section](link) in the Demystifying Regular Expressions module shows and example of how to use the website.

## Simple Regular Expressions

To describe a pattern, you need to indicate what characters you expect to see using **tokens**, and how many of them, using **quantifiers**.  Tokens can be very simple and intuitive (the token for expressing the letter "A" is just `A`) or can be more complex (the token for any digit 0-9 is `\d`).  Quantifiers can be symbols such as `*` or `+`, or can include a number (the quantifier for "exactly two" is `{2}`).

We'll work with simple regular expressions in this module by describing two principal tasks you need to do in regex: 

1. Indicating which characters are valid at a given point in a pattern with various kinds of tokens. 
2. Quantifying how many of those characters you expect to find there using quantifiers.

Soon, the mysterious set of symbols that makes up a regular expression will make sense and not feel like random characters!


### Tokens: Indicating a Specific Character

Let's start with a very simple pattern: one looking for a specific character or character sequence.  You might want to express that your pattern is "the letter `A`" or "the number `93`" or "the characters `mg/dL`".  

Letters and numbers
------

* Any given letter or number, like the character "u", can be used as-is: `u` is the regular expression that matches the lowercase letter "u", `7` is the token matches the number 7.
* You can put several of these in a row.  If your pattern starts with the characters "2023ABC", you write that in a regular expression as `2023ABC`.  

Spaces
-----

* If your pattern includes a space (the kind you would get from hitting the space bar), you can just put a space in.  `A cat`, for example, is the regular expression that will match the sequence of the letter `A`, a space, and the letters `c`,`a`, and `t`.
* Other types of spaces are entered using special tokens.  A tab is represented by `\t`, new line by `\n`, and the carriage return as `\r`.

Symbols
------

* Some non-alphanumeric symbols, like the underscore (`_`), hash mark (`#`), percent (`%`), and equals (`=`), can also just be put in as-is: `%` is the regular expression that matches the percent sign (%), and `#` matches the hash mark (#).
* There are other symbols called **metacharacters** that have special meanings in regular expressions, and indicating you want to look for those symbols is slightly trickier. 
* It can be hard to remember which symbols are metacharacters, but that comes with practice.

On the next page, we'll learn about metacharacters.


### Tokens: Metacharacters

The following **metacharacters** are symbols that have special meaning in regex.  This means that if you want to add these symbols to a pattern, you'll need to indicate you are referring to the literal character, and not using the symbol in its special regex way.  

`. ^ $ * + ? { } [ ] \ | ( ) - /`

If you want to refer to one of these special characters in regex (for example, if your pattern includes square brackets or parentheses or periods), you can add a backslash (` \ `) just before the symbol. The backslash in regex does a couple of different things, but here, the use of a backslash indicates "I mean this character literally, I'm not using this character's special powers." This is called **escaping** or an **escape sequence**.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Sometimes the hyphen (`-`) and the forward slash (`/`) are not included in lists of metacharacters, because these two characters only have a special function in certain contexts, not all the time.  We include them in our list of metacharacters here because they do *sometimes* have a special function, and you can put a backslash in front of them to indicate you mean the literal symbol and not its special meaning.  

In most uses of regex, if you're not sure if a (non-alphanumeric) character has a special meaning or not, you can put a backslash in front of it just in case.  So, for example, the hash symbol `#` doesn't have a special function in regex.  But if you weren't sure, you can usually add the backslash, giving `\#` to indicate `#`.  It's not required, but most regular expression parsers will realize what you mean.

</div>

* To indicate a question mark in your pattern, you'd escape it like this: `\?`.
* A period would similarly use the backslash: `\.`
* Want to indicate a left curly brace? `\{`
* Vertical pipe? `\|`
* A backslash itself?  `\\ `
* A hyphen/dash? `\-`
* A percent sign? Either `%` by itself, because it's not a metacharacter, or `\%` because you weren't sure and added the escape sequence just in case.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Don't try to use the backslash this way in front of letters or numbers. If you add `\d` to your pattern, for example, that doesn't mean "the literal letter d", it means "any digit 0-9".  If you add `\7` to your regular expression, you'll get an error -- `\7` is bad syntax for regular expressions. 

We'll talk about other uses of backslash in an upcoming section.

</div>

Combining letters, numbers, spaces, symbols, and escape sequences
----

You can combine escaped characters and normal characters.  For example, if your pattern includes ".co.nz #5", you would express that as `\.co\.nz #5`.

### Quiz: Specific Characters

Which regular expression below will match the text "25% (20) claim:"?  Check all that apply.

[[X]] `25\% \(20\) claim\:`
[[X]] `25% \(20\) claim:`
[[ ]] `25% (20) claim:`
[[ ]] `25\% (20) claim\:`
[[?]] Hint: Feeling stuck?  Try using [Regex 101](https://www.regex101.com) and plug in the regex patterns given in the answers as well as the test string posed in the question.
***
<div class = "answer">

Let's take this character by character.

* `25` can be put in the pattern just as it appears: `25`.
* `%` is not a metacharacter for regex, so you can add it as is, with `%`, or, if you weren't sure if `%` was a metacharacter, you can also "escape" it, giving `\%`.
* The space after the percent can be added as is: ` `
* The opening parenthesis is a metacharacter, so it **must** be added to the pattern with a backslash: `\(`
* The numbers `20` should be added as is: `20`
* The closing parenthesis is a metacharacter, so it **must** be added to the pattern with a backslash: `\)`
* The space after the closing parenthesis can be added as-is:  ` `
* The letters `claim` can be added just as they appear: `claim`
* `:` is not a metacharacter for regex, so you can add it as is, with `:`, or, if you weren't sure if `:` was a metacharacter, you can also "escape" it, giving `\:`.

This means that either `25\% \(20\) claim\:` or `25% \(20\) claim:` are regular expressions that match the given text.  On the other hand, `25% (20) claim:` and `25\% (20) claim\:` do not match the given text, because they fail to escape the parentheses.

</div>
***

### Tokens: Special Groups

Often, we want to indicate that a group of characters are all equally valid in a location.  For example, a pattern might include any digit at all in a particular location, or any of the letters A, Q, or Y at another location.  This is very typical, and this is where regular "find" or "find and replace" tools in software fail, while regular expressions prove useful.

There are several ways to indicate groups of possible characters, and we'll go over the most common ones next.

Lists
-----

Groups of characters can be added to a custom **list**.  Each member of the custom character set is added to a list, with no separators, that appears between square brackets.

* One of the letters `Y` or `N` could be written as `[YN]` (or `[NY]`)
* Either the number 0 or the number 1? `[01]` (or `[10]`)

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Don't include separators in your list!  `[Y,N]` is not the same as `[YN]`.  The first is a token that represents "either `Y`, or a comma (`,`), or `N`," and the second is a token that represents "either `Y` or `N`."

</div>

You can combine list tokens with other tokens.  For example, if the pattern we're describing begins with a single "A", then a hyphen, then either a "Y" or "N", we would write that in regex as `A\-[YN]`.

Metasequences
------  

The list of all digits and some other lists of characters are so commonly used they are predefined with special **metasequences**.  Writing `[0123456789]` is valid, but there's a shorter way to express it: `\d`.

* Any single digit (0, 1, 2,... 8, 9) is represented `\d`.  
* Any whitespace character like space or tab? That's `\s`.
* Any character at all (called a **wildcard**)? Type a single period `.`

You can combine these metasquence tokens with what we've already learned.  For example, if the pattern we're trying to define includes a single digit, the letter Z, some other character that could be anything, and the letter J, we could put that in a regular expression as `\dZ.J`.

Ranges
-----

You can also use square brackets to define a **range** of characters, giving a beginning character followed by a dash and then an ending character.  Let's start with numbers, to give you an idea of how ranges work.

* Any digit 0-7 can appear, but not other digits? `[0-7]` is the token that gives that range.  It's a lot shorter than typing `[01234567]`!

You can add a range and also list individual characters, being careful not to add separators.

* Let's say your subject identifiers, depending on where they originated from, could begin with "A" or "C" or any digit 1-4.  You could define the pattern for the first character of your subject identifier as `[AC1-4]` or `[CA1-4]` or `[1-4CA]`, etc.
* Maybe a character will either be 0, 2, 5, 6, 7, or 8.  You could include the two individual numbers 0 and 2 and the range 5-8 like this: `[025-8]`. 

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Remember that a token represents a **single character**, so it might be helpful to read something like `[025-8]` aloud one character at a time: say "zero or two or five through eight" to yourself instead of "twenty five through eight," which is confusing!

</div>

You can even put two or more ranges in square brackets, right next to one another.  Again, don't put a separator between your two ranges.

* Any digit 0-3 or 7-9? The token `[0-37-9]` represents a single character that falls into one of the two possible ranges 0-3 or 7-9.


<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

Characters, whether they are numbers, letters, other symbols, or whitespace, are represented in [Unicode](https://en.wikipedia.org/wiki/List_of_Unicode_characters). Unicode includes over 100,000 characters, each of which has a hexidecimal (base 16) code associated with it. When we give a range in a regular expression, we're actually giving the character range in the underlying Unicode.  For example, in the range `[1-4]`, we're actually referring to the Unicode characters U+0031 (`1`) through U+0034 (`4`) and saying that any Unicode character between (and including) U+0031 and U+0034 is acceptable.

Unicode tends to keep sets of character in order, abiding by previous conventions.  For example, the digits appear in order from `0` (U+0030) to `9` (U+0039).  Letters also appear in Unicode in their typical order.   `A` (U+0041) is followed by `B` (U+0042), and so on, until `Z` (U+005A).  

The ordering of things that we don't have a specific order for, like punctuation, or sets themselves, can feel a little arbitrary, and it can be helpful to look up [Unicode characters](https://en.wikipedia.org/wiki/List_of_Unicode_characters) to see what order things are in.  For example, between the digit `9` and the letter `A`, the following characters appear in Unicode:

| Symbol  | Unicode value |
| :--------- | :--------- |
| Colon (`:`)   | U+003A |
| Semicolon (`;`)   | U+003B |
| Less-than sign (`<`)   | U+003C |
| Equal sign (`=`) | U+003D |
| Greater-than sign (`>`)   | U+003E |
| Question mark (`?`)  | U+003F |
| At sign (`@`)  | U+0040 |


</div>


Letters
----

Letters are tricky because they can have two cases and also have various diacritics.  Each of these sets appears in a different place in Unicode. Let's take a closer look:

* Any uppercase (unaccented) letter could appear in the pattern?  `[A-Z]` indicates the Latin letters A to Z. `[A-F]` indicates just the first six letters.
* Any lower case Latin letter? `[a-z]`.  Only a subset? `[c-h]` is the range that is a shorter way of writing `[cdefgh]`.
* Upper and lower? You can do two ranges: `[A-Za-z]` or `[A-Fa-f]`.
* `[A-Za-zÀ-ÿ]` will additionally give you [accented letters and letters with circumflex, umlaut, etc.](https://en.wikipedia.org/wiki/List_of_Unicode_characters#Latin_script:~:text=%23-,Latin%20Extended%2DA,-%5Bedit%5D) that belong to European languages.  However, this range also happens to span the Unicode range that includes some math characters, namely `×` and `÷`.
* `[A-Za-zÀ-ÖØ-öø-ÿ]` gives you all the European letters and excludes `×`, and `÷`.
* Need to add [Cyrillic](https://en.wikipedia.org/wiki/List_of_Unicode_characters#Cyrillic)? That's this range: `[Ѐ-ӿ]`
* There are other language-specific ranges to consider, and you can find the starting and ending symbols to put as the range by looking at a [list of unicode characters](https://en.wikipedia.org/wiki/List_of_Unicode_characters).
* Using letters in a language that is written right to left?  The range should also be written and read right to left!  For example, the Hebrew alphabet (without diacritics) can be written `[א-ת]`.  Combining two ranges?  Each range should be in the direction of its language: `[א-תA-Z]`


<div class = "options">
<b style="color: rgb(var(--color-highlight));">Another option</b><br>
Another way to indicate a range of Unicode characters is to use the Unicode number of the symbol.  For example, the [Hebrew](https://en.wikipedia.org/wiki/List_of_Unicode_characters#:~:text=Unicode%20version%206.0-,Hebrew,-%5Bedit%5D) letter א (Aleph, the first letter of the hebrew alphabet) appears in Unicode as U+05D0.  The letter ת (Tav, the last letter) is at U+05EA.

You might have an English-only keyboard and only know how to add Hebrew letters by copy-paste.  That's a pain, especially if you're going to refer to these letters a few times.  Also, you might not be sure what order to put the range in, using the actual letters.  After all, regex is typically written left to right, but Hebrew is written right to left. Is the correct form `[ת-א]` or `[א-ת]`?  Tricky! 

In cases like this, where you can't easily type a symbol, you may instead want to indicate Unicode positions using `\x` followed by the four digit Unicode position (depending on the regex parser, you might add the number with or without enclosing curly braces).  Therefore, if you wanted the alphabet starting with א , you could use `[א-ת]`(because Hebrew is written right to left, this range is written in that direction) or `[\x{05D0}-\x{05EA}]`.  Unicode ranges are written left to right, regardless of the underlying symbols.

Try the correct [right-to-left range notation of `[א-ת]`](https://regex101.com/r/9B6mzl), the incorrect [left-to-right range notation of `[ת-א]`](https://regex101.com/r/aODZog), and the correct [unicode range notation of `[\x{05D0}-\x{05EA}]`](https://regex101.com/r/z8Ygap/1) in Regex 101!

</div>



### Quiz: Metasequences, Lists, and Ranges

This the regular expression that represents the valid characters that can appear in the first part of an email address (the part before the `@`):

`[A-Za-z\d\-\._]`

**According to this regular expression** (which for simplicity's sake isn't reflective of all of the rules for email addresses in reality), which of the following characters can appear in the first part of an email address?  Check all that apply.

[[ ]] `\ `
[[X]] `9`
[[X]] `_`
[[ ]] `!`
[[X]] `.`
[[ ]] `ö`
[[X]] `o`
[[X]] `O`
[[X]] `-`
[[ ]] ` ` (space)
[[?]] Hint: Feeling stuck?  Try using [Regex 101](https://www.regex101.com) and plug in the regex pattern given in the question as well as the test characters in the answers.
***
<div class = "answer">

Let's look at the regular expression.

* `A-Za-z` indicates that all unaccented upper and lowercase Latin letters are included, so `o` and `O` are valid for the first part of an email address.  However, `ö` is left out and not included.
* `\d` indicates that any digit is acceptable as well, so `9` is valid.
* `\-` indicates that a literal hyphen / dash is included in our character set, so `-` is valid.
* `\.` indicates that a literal period is included in our character set, so `.` is valid.
* `_` indicates an underscore, so `_` is also acceptable.

There is no mention of a literal backslash, exclamation point, or space, so those are all excluded, as is our letter with an umlaut: `ö`.

</div>
***

### Quantifiers: How Many Characters?

So far, we've gone over single characters like `7`, lists like `[YN]`, metasequences like `\d`, and ranges like `[0-9]`, all to define what's valid for a single character in a pattern.  These ways to define what a character could be are collectively called **tokens**.  

However, there's more to patterns than defining tokens one character at a time.  Usually, patterns have a certain number of characters in a row that are all represented by the same token, like five digits or three letters.  It would be very annoying to have to put `\d\d\d\d\d` (five digits) or `[A-Za-z][A-Za-z][A-Za-z]` (three letters) to represent these patterns.  And what if there's a varying length?  Three to five digits, or four or more letters?  That's where **quantifiers** come in!

Sometimes we know there should be exactly one of something (for example, exactly one `@` in an email address).  Sometimes there can be an optional character (like the optional parentheses around the area code of a U.S. phone number).  Sometimes there are a specific number of characters from the same group (like exactly three letters or five digits).  Maybe there's a range, such as at least 2 letters but not more than 20.  

Regular expressions allow you to quantify characters in a pattern.  You do this by adding a quantifier after your token.

* An optional token, which might not appear at all or might appear at most once can be represented with a `?` quantifier.  For example, a phone number pattern that might begin with the number 1 or might omit it could begin with `1?`
* An optional token that could repeat zero, one, or multiple times can be quantified with an asterisk (`*`).  For example, a phone number can have an optional extension that has one, two, or more digits.  That could be represented as `\d*`.
* At least one character, maybe more? That's `+`. So, a first name has to have at least one letter, but could have more: `[A-Za-z]+`
* A specific range, like one to three, but not less than one or more than three? That's `{1,3}`.  For example, maybe you know that in your health system, medical record numbers could have 9, 10, or 11 digits: `\d{9,11}`
* An open ended range, such as "two or more" can be written by omitting the upper boundary: `{2,}`.

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Regex rules can be confusing, and even after lots of practice using regular expressions, it can be time saving and helpful to use a regex checker like [Regex 101](https://www.regex101.com) to test out your pattern with some sample strings.  Add your pattern and put in a few test strings -- some that match your desired pattern, and some that don't, so you can see if you're getting the pattern description right in your regex code.

</div>

### Quiz: Putting It All Together 

The regular expression that gives the pattern for American Express credit card numbers is given as:

`3[47]\d{13}`

Which of the following is true?  Select all that apply.

[[ ]] American Express credit card numbers start with `347`.
[[X]] American Express credit card numbers start with `34` or `37`.
[[ ]] American Express credit card numbers start with `3` or `47`.
[[ ]] American Express credit card numbers have 13 digits.
[[X]] American Express credit card numbers have 15 digits.
[[ ]] American Express credit card numbers have 16 digits.
[[ ]] American Express credit card numbers have a flexible number of digits.
[[?]] Hint: Feeling stuck?  Try using [Regex 101](https://www.regex101.com)!
***
<div class = "answer">

Let's parse `3[47]\d{13}`.  This pattern indicates that American Express credit card numbers:

* Begin with a `3`
* Are followed with either a `4` or a `7`
* Then include 13 digits between `0` and `9`, inclusive.

This means that American Express credit card numbers will start with `34` or `37` and will have 15 digits.

</div>
***

## Additional Resources

We only scratched the surface of regular expressions.  Want to learn more?

Here are some good cheat sheets:

* [Dave Child's cheat sheet](https://cheatography.com/davechild/cheat-sheets/regular-expressions/) is fairly comprehensive.
* [DataCamp's cheat sheet for regex](https://images.datacamp.com/image/upload/v1665049611/Marketing/Blog/Regular_Expressions_Cheat_Sheet.pdf) is another good option.

If you want to check out regular expression checkers, here are a few we like:

* [Regex 101](https://regex101.com) is the regular expressions tester used in this module.  We use it regularly, even after working with regular expressions for many years.
* [RegExr](https://regexr.com/) has helpful teaching aids, including a hover-over explainer that allows you to investigate matches, and a way to look at complex nested elements (for instance, a range of characters inside square brackets inside a capturing group) in a visual way.
* [RegEx Testing](https://www.regextester.com/) has a clean, simple interface and a library of popular regular expressions to start with. 

Wondering about Unicode character ranges?  

* Check out Wikipedia's [list of Unicode characters](https://en.wikipedia.org/wiki/List_of_Unicode_characters) to copy/paste characters you're not sure how to type (like ǔ or Ǣ or Ƣ) and to see the beginning and ending characters for ranges you'd like to include in patterns.
* Or look at [Unicode blocks](https://en.wikipedia.org/wiki/Unicode_block) to define ranges by their Unicode numbers.  For example, Tagalog Baybayin script characters are from U+1700 to U+171F.

## Feedback

@feedback
