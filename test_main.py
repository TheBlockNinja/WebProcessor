from driver.WebProcessor.WebProcessor import WebProcessor
from driver.WebProcessor.WebFilter import WebFilter

wb = WebProcessor(show_window=False,req_user_input=True)
wb.load()
wb.load_page("https://github.com/TheBlockNinja/WebProcessor")

wf = WebFilter()
if not wf.load_filter("test_filter.json"):
    wf.add_filter_data(wf.filter_tag,"link")
    wf.add_filter_data(wf.filter_attribute,"href")
    wf.add_filter_data(wf.filter_contains,"png")
    wf.save_filter("test_filter.json")

data = wf.filter_elements(wb)
print(data)

for i in range(len(data)):
    wb.download_img(file_name="test_"+str(i)+".png", direct=True,url=data[i])

wb.stop()