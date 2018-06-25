The project is to download the images from Google search.
<br>
Input : any search tag.
<br>
Output : images downloaded from google search using the tag.
<br>

How to make it work : 
* run command **python scrape_images.py -q="your_search_tag"**
* BASE_URL in the scrape_image.py file can be customized according to the requirement. How to do that is mentioned in 
the comments in the file.
  
_P.S. : Search tag if contains more than one word should be passed by combining using '\_' like red apple should be 
passed as -q=red\_apple_
