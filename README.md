# JSON-Search-Engine-Python
>This is a search engine used to find a recipe that are stored in a JSON file (provided) based on the keywords provided and to find complete recipes when the exact name is given.
>There are 2 main modes of using the search engine

![](header1.png)
![](header2.png)

## Prerequisite

This game utilises the json, string modules to function:
```python
import json
import string
```
It requires a JSON file to read the data from.

## How To Use 
>To run the search engine, run main.py
>There are 2 modes to choose from 
>1. Recipe Finder Using Keywords
>2. Recipe Lookup Using Name

## Recipe Finder Using Keywords
>The user needs to input 3 main fields for the search.
> ### Keywords: 
> #### Enter All The Words That You Would Like To See In Your Recipe
> ### Search Type:
> #### 1. Normal: The most basic search, the recipes are ordered by the maximum occurerences of the keywords.
> #### 2. Simple: Provides you with the recipes that have the least number of indegredients and directions.
> #### 3. Healthy: Certain recipes have nutritional values provided, using a special formula we sort the food items from most healthy to least healthy.
> ### Amount Of Recipes:
> #### Allows The User To Input The Number Of Recipes They Would Like To See.

## Recipe Lookup Using Name
>The User Needs To Input The Exact Name As Given In The Recipe Search Tool in Mode 1
>If A Recipe Is Found It's Title:, Categories:, Ingredients: and Directions: Will Be Displayed.

## Use Your Own JSON FIle
>This search engine is a simple tool that can be edited based on your prefrence. If you have a JSON data file with a structure similar to the recipes.JSON file provided, a few minor changes can be made to the code to search the data in your .JSON file.

## Release History

* 1.0.0
    * Final Release
* 0.3.1
    * Bug Fixes
* 0.3.0
    * Improved UI to make unlimited searches and bug fixes
* 0.2.1
    * Added "Recipe not found message" when there was no match.
* 0.2.0
    * Added Recipe lookup mode to display the entire recipe.
* 0.1.2
    * Fix: Program Crash When Recipie Not Found.
* 0.1.1
    * Added a simple console based UI 
* 0.1.0
    * The first proper release (only mode 1)
* 0.0.1
    * Work in progress

## Meta

Hoshner Tavadia – hoshnertavadia@gmail.com

Distributed under the GPL-3.0License. See ``LICENSE`` for more information.

[https://github.com/tavadia-hoshner/](https://github.com/tavadia-hoshner/)
