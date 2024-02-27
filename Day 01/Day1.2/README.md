# HTML Introduction

What is HTML?
HTML (HyperText Markup Language) was created by Tim Berners-Lee in 1991 as a standard for creating web pages. It's a markup language used to structure content on the web, defining elements like headings, paragraphs, links, and images. HTML forms the backbone of web content. In layman's terms, HTML is like the skeleton of a website. It's a set of instructions that tells a web browser how to display text, images, videos, and other elements on a webpage. Think of it as the building blocks that create the structure and look of a website, similar to how bricks and mortar are used to build a house.

In a nutshell:

HTML is the language of the web, used to create websites.
HTML defines the barebone structure or layout of web pages that we see on the Internet.
HTML consists of a set of tags contained within an HTML document, and the associated files typically have either a ".html" or ".htm" extension.
There are several versions of HTML, with HTML5 being the most recent version.
Features of HTML
It is platform-independent. For example, Chrome displays the same pages identically across different operating systems such as Mac, Linux, and Windows.
Images, videos, and audio can be added to a web page (For example - YouTube shows videos on their website)
HTML is a markup language and not a programming language.
It can be integrated with other languages like CSS, JavaScript, etc. to show interactive (or dynamic) web pages
Why the Term HyperText & Markup Language?
The term 'Hypertext Markup Language' is composed of two main words: 'hypertext' and 'markup language.' 'Hypertext' refers to the linking of text with other documents, while 'markup language' denotes a language that utilizes a specific set of tags.

Thus, HTML is the practice of displaying text, graphics, audio, video etc. in a certain way using special tags.

Note: Tags are meaningful texts enclosed in angle braces, like '<...>'. For example, the '<head>' tag. Each tag has a unique meaning and significance in building an HTML page, and it can influence the web page in various ways.

## HTML Page Structure
An HTML document is structured using a set of nested tags. Each tag is enclosed within <…> angle brackets and acts as a container for content or other HTML tags. Let's take a look at a basic HTML document structure:

```bash
<!DOCTYPE html>
<html>
<head>
    <title>Document</title>
</head>
<body>
   <!-- content -->
</body>
</html>


## HTML Comments
Comments in HTML are like little notes you leave in your code for yourself or other people. These notes help make the code easier to understand but don't show up on the actual website. The web browser just skips over them!

Key Points About HTML Comments
Comments are ignored by web browsers.
They aid in code readability and documentation.
HTML comments are denoted by <!-- content -->.
The shortcut key for commenting out code is Ctrl + /.
HTML supports both single-line and multi-line comments.
Types of Comments in HTML
HTML primarily supports two types of comments:

### Single-line Comments
Single-line comments are contained within one line. They are useful for short annotations.

Example:
```bash
<!-- This is a single-line comment -->

### Multi-line Comments

Multi-line comments span across multiple lines, making them ideal for detailed explanations or temporarily disabling blocks of code.

Example:

```bash
<!-- 
This is a multi-line comment.
It spans multiple lines.
-->

