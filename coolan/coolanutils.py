from coolan.x_app_token import generate_token

class CoolMarketHeaders:
    def __init__(self):
        self.cookies  = {
        'uid': '22734105',
        'username': 'ken%E5%95%A6%E5%95%A6%E5%95%A6%E5%95%A6%E5%95%A6',
        'token': '692c50d5pGjdwI4QmBGHppkpyivY13DdMpH2o8sKXs1D62iHKlqTmFXm1cWLwDqPcbzR1tyBxVOv-B_oN6cw7sXlghBphuQhNGpmPgBzLIzsAIqubM3xKZzTjsj6t9zZTJ-i1hRWYIkwTajYT5GhW2CXB10vELxNMTKb4M876yi2x0kPhDAOekFlcqflQUMKRemNZNrrO3-rQ-pfqKunfM2BmCPCDA',
    }
        self.headers = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 13; 22041211AC Build/TP1A.220624.014) (#Build; Redmi; 22041211AC; TP1A.220624.014; 13) +CoolMarket/13.0.1-2301171-universal',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Sdk-Int': '33',
        'X-Sdk-Locale': 'zh-CN',
        'X-App-Id': 'com.coolapk.market',
        'X-App-Token': generate_token(),
        'X-App-Version': '13.0.1',
        'X-App-Code': '2301171',
        'X-Api-Version': '13',
        'X-App-Device': 'IWN4UWZ4MjMiJWO5YGM1IGI7QTMw4CNyYDMyIjLBFDUUByODFUMxITM0AjMyAyOp1GZlJFI7kWbvFWaYByOgsDI7AyOhhjS3Jje5AzcHpnSBJXOwNXTjJzVk9mV1EnTE9FNChDeIVFR',
        'X-Dark-Mode': '1',
        'X-App-Channel': 'coolapk',
        'X-App-Mode': 'universal',
        'X-App-Supported': '2301171',
        'Host': 'api.coolapk.com',
        'Connection': 'Keep-Alive',
    }

# 创建 CoolMarketHeaders 类的实例
cool_market_headers = CoolMarketHeaders()


