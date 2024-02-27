# Image Tag
Images play a crucial role in enhancing web pages by providing a visual context that complements textual content. In HTML, the <img> tag is used to embed images into web pages.

## Key Features of the <img> Tag
It's a self-closing tag, meaning it doesn't require a corresponding closing tag.
Commonly used attributes include the "alt" attribute for image descriptions and the "src" attribute for specifying the image location.
Supports various image formats including PNG, JPEG, JPG, and GIF.

## Setting Mandatory Attributes
The "src" and "alt" attributes are essential for the proper functioning of the <img> tag.

src attribute: Specifies the path to the image file.
alt attribute: Provides a text description for the image.

Note: To find the image's location, right-click on the image, go to properties, and check the location field.

## Setting Image Dimensions
Although dimensions can be set using the "width" and "height" attributes in the <img> tag, modern best practices recommend using CSS for this purpose.

Setting the width and height attributes for images in HTML can have a positive impact on Search Engine Optimization (SEO). Specifying these dimensions in the <img> tag allows browsers to allocate the correct amount of space on a web page even before the image is fully loaded. This prevents layout shifts, improving the Cumulative Layout Shift (CLS) score—a key metric in Google's Core Web Vitals. A better CLS score can lead to a higher page ranking in search engine results.

Note: Styling dimensions and other properties are now more commonly managed through CSS for better flexibility and maintainability.

# HTML Lists
Our day-to-day lives often involve the use of lists. For example, when we go shopping, the bill we receive includes a list of all the items we've purchased. In a similar manner, web developers use lists to neatly display data on websites.

## Types of HTML Lists
HTML provides different types of lists to display data in various forms. Each list contains one or more list items.

Unordered List: Displays items using bullets.
Ordered List: Displays items in a numerical sequence, and supports various numbering styles like Arabic numerals, Roman numerals, and so on.
Definition List: Organizes items in a format similar to a dictionary, with terms and their corresponding definitions.


# HTML Tables
HTML tables allow you to arrange data like text, images, and links in rows and columns. You use the <table> tag to start and end a table.
    
## Key Elements of HTML Table
<table> 
    Defines the table itself.
<tr> 
    Used for table rows.
<th> 
    Used for table headings.
<td> 
    Used for table cells (data).

## rowspan and colspan Attributes
Rowspan: If you want a table cell to span multiple rows, you can use the rowspan attribute.

    
Colspan: If you want a table cell to span multiple columns, you can use the colspan attribute.

    
