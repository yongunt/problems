def nearest_chapter(chapters:dict, page:int) -> str:
    ans:str = list(chapters.items())[0][0]
    ans_page:int = chapters[ans]

    for chapter in chapters:
        if abs(chapters[chapter] - page) < abs(page - ans_page):
            ans = chapter
            ans_page = chapters[chapter]
        elif abs(chapters[chapter] - page) == abs(page - ans_page) and ans_page < chapters[chapter]:
            ans = chapter
            ans_page = chapters[chapter]

    return ans


print(nearest_chapter({
  "Chapter 1" : 1,
  "Chapter 2" : 15,
  "Chapter 3" : 37
}, 10))


print(nearest_chapter({
  "New Beginnings" : 1,
  "Strange Developments" : 62,
  "The End?" : 194,
  "The True Ending" : 460
}, 200))


print(nearest_chapter({
  "Chapter 1a" : 1,
  "Chapter 1b" : 5
}, 3))


'''
nearest_chapter({
  "Chapter 1" : 1,
  "Chapter 2" : 15,
  "Chapter 3" : 37
}, 10) ➞ "Chapter 2"


nearest_chapter({
  "New Beginnings" : 1,
  "Strange Developments" : 62,
  "The End?" : 194,
  "The True Ending" : 460
}, 200) ➞ "The End?"


nearest_chapter({
  "Chapter 1a" : 1,
  "Chapter 1b" : 5
}, 3) ➞ "Chapter 1b"
'''