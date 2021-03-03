from driver.WebProcessor.WebProcessor import WebProcessor

wb = WebProcessor(show_window=False)
wb.load()
wb.load_page("https://github.com/TheBlockNinja/WebProcessor")

filter_elements = {
    "1_tag" : "link",
    "2_attribute" : "href",
    "3_contains" : "png"
}

data = wb.filter_elements(filter_elements)
print(data)

for i in range(len(data)):
    wb.download_img(file_name="test_"+str(i)+".png", direct=True,url=data[i])
wb.stop()