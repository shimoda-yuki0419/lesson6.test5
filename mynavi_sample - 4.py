import os
from selenium.webdriver import Chrome, ChromeOptions
import time
import pandas as pd
import csv


### Chromeを起動する関数
def set_driver(driver_path,headless_flg):
    # Chromeドライバーの読み込み
    options = ChromeOptions()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg==True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    #options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    return Chrome(executable_path=os.getcwd() + "\\" + driver_path,options=options)

### main処理
def main():
    search_keyword=input("")
    # driverを起動
    driver=set_driver("chromedriver.exe",False)
    # Webサイトを開く
    driver.get("https://tenshoku.mynavi.jp/")
    time.sleep(5)
    # ポップアップを閉じる
    driver.execute_script('document.querySelector(".karte-close").click()')
    time.sleep(2)
    # ポップアップを閉じる
    # driver.execute_script('document.querySelector(".karte-close").click()')
    
    # 検索窓に入力
    driver.find_element_by_class_name("topSearch__text").send_keys(search_keyword)
    # 検索ボタンクリック
    driver.find_element_by_class_name("topSearch__button").click()
    

    # 1ページ分情報取得
    
        
       
    # 終わるまで処理
    next_page=driver.find_elements_by_class_name("iconFont--arrowLeft")
    if len(next_page)>=1:
        next_page_link=next_page[0].get_attribute("href")
        driver.get(next_page_link)
    else:
        print("最終ページです。終了します。")
             
    elem_names = driver.find_elements_by_class_name("cassetteRecruit__name")
    elem_characteristics = driver.find_elements_by_class_name("cassetteRecruit__copy")
    elem_contents = driver.find_elements_by_class_name("tableCondition__body")
    print(len(elem_names))
    print(len(elem_characteristics))
    print(len(elem_contents))
    for elem_name,elem_characteristic,elem_content in zip(elem_names,elem_characteristics,elem_contents):
           print(elem_name.text)

    elem_name_list=[]
    elem_name_list.append[elem_name.text]
    elem_characteristic_list=[]                            
    elem_characteristic_list.append[elem_characteristic.text]
    elem_content_list=[]
    elem_content.append[elem_content.text]                       
    
    df = pd.DataFrame({
        '会社名':elem_name_list,
        '特徴':elem_characteristic_list,
        '内容':elem_content_list}
    )

    
                        
                    
    df.to_csv("./mynavi.csv",mode="a",encoding="utf_8_sig")

    

    
    
        

                                        

### 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
