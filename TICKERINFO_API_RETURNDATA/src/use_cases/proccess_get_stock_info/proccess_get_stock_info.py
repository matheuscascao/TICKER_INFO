from TICKERINFO_API_RETURNDATA.src.entities.News import News, Stock
from TICKERINFO_API_RETURNDATA.src.use_cases.proccess_get_stock_info.dto_get_stock_info import StockInfoDtoInput, StockInfoDtoOutput

# lista_teste = [
# 		{
# 			"source": {
# 				"id": "engadget",
# 				"name": "Engadget"
# 			},
# 			"author": "https://www.engadget.com/about/editors/kris-holt",
# 			"title": "Microsoft rolls out Teams Premium with OpenAI-powered features | Engadget",
# 			"description": "Microsoft says Teams Premium uses tech like OpenAI’s GPT-3.5 to make meetings 'more intelligent, personalized and protected.'.",
# 			"url": "https://www.engadget.com/microsoft-teams-premium-openai-artificial-intelligence-152658424.html",
# 			"urlToImage": "https://s.yimg.com/os/creatr-uploaded-images/2023-02/c6a72050-a30c-11ed-8fed-e59b58ee140e",
# 			"publishedAt": "2023-02-02T15:37:20.4674475Z",
# 			"content": "Fresh off the heels of news that Microsoft\r\n is making a multibillion-dollar investment into OpenAI\r\n, its integrating the companys tech into more of its products and services. Microsoft has announce… [+1074 chars]"
# 		},
# 		{
# 			"source": {
# 				"id": "the-verge",
# 				"name": "The Verge"
# 			},
# 			"author": "Tom Warren",
# 			"title": "Microsoft launches Teams Premium with features powered by OpenAI",
# 			"description": "Microsoft Teams Premium is now generally available. It includes as new AI-powered intelligent recap feature that may tempt businesses to pay extra.",
# 			"url": "http://www.theverge.com/2023/2/2/23582610/microsoft-teams-premium-openai-gpt-features",
# 			"urlToImage": "https://cdn.vox-cdn.com/thumbor/rmWEVoDVWWbcsRx_I0m-045sp68=/0x0:2640x1760/1200x628/filters:focal(1320x880:1321x881)/cdn.vox-cdn.com/uploads/chorus_asset/file/19344713/microsoftteams.jpg",
# 			"publishedAt": "2023-02-02T12:17:16Z",
# 			"content": "Microsoft launches Teams Premium with features powered by OpenAI\r\nMicrosoft launches Teams Premium with features powered by OpenAI\r\n / Teams Premium includes an AI-powered intelligent recap feature, … [+2991 chars]"
# 		},
# 		{
# 			"source": {
# 				"id": "recode",
# 				"name": "Recode"
# 			},
# 			"author": "Sara Morrison",
# 			"title": "Thanks to OpenAI, Microsoft is beating Google in the artificial intelligence game",
# 			"description": "The software stalwart’s big investment in AI could make it cutting-edge again.",
# 			"url": "https://www.vox.com/recode/2023/1/26/23571710/microsoft-open-ai-chatgpt-google",
# 			"urlToImage": "https://cdn.vox-cdn.com/thumbor/XNDnN6sZMeXD1hnRm8DgsXZ0Xqg=/0x0:5472x2865/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/24385993/GettyImages_1459359021.jpg",
# 			"publishedAt": "2023-01-26T13:00:00Z",
# 			"content": "Microsoft appears to be on the cusp of being something it hasnt been in a long time: cutting-edge. Its a label the company lost a long time ago after a series of small startups grew to become Microso… [+5986 chars]"
# 		},
# 		{
# 			"source": {
# 				"id": "ign",
# 				"name": "IGN"
# 			},
# 			"author": "Eric Song",
# 			"title": "Daily Deals: Save $50 Off the Microsoft Xbox Series X Gaming Console + Elite Series 2 Wireless Controller Bundle - IGN",
# 			"description": null,
# 			"url": "https://www.ign.com/articles/daily-deals-microsoft-xbox-series-x-gaming-console-elite-series-2-controller",
# 			"urlToImage": "https://assets-prd.ignimgs.com/2022/09/01/090122-1662050863587.jpg?width=1280",
# 			"publishedAt": "2022-09-01T17:05:23Z",
# 			"content": "Check out the new hot daily deals for today, including a rare discount on an Xbox Series X gaming console bundle, $170 off the Apple AirPods Max headphones, $50 off the Bose SoundLik II portable Blue… [+12798 chars]"
# 		}
# 	]

class ProccessCreateStock():
    def execute(self, input: StockInfoDtoInput) -> StockInfoDtoOutput:
        output = StockInfoDtoOutput()
    
