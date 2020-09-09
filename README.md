# OpenWPM Introductory Project

## Introduction

In this mini-project, I conducted measurements to analyze the impact of using ad blocking extensions on top-100 websites, specifically comparing the third-party HTTP(S) requests, third-party cookies, and JavaScript API calls made by a browser in the “ad blocking mode” (ad blocking extension enabled) and the “vanilla mode” (ad blocking extension disabled).
 
## External Resources
I used an open source tool OpenWPM (https://github.com/citp/OpenWPM) for visiting websites to record HTTP(S) requests, cookies, and JavaScript API calls. The uBlock Origin extension for ad blocking is already built-in OpenWPM.
 
Please consult the instructions provided on the official Github page of OpenWPM (https://github.com/citp/OpenWPM) for further assistance.


## Third-Party HTTP Requests
![http.png](/http.png)

### Top-10 Third Party Domains (HTTP Requests)
|Vanilla|Adblock|
|--|--|
|<table> <tr><th>Domain</th><th>HTTP Requests</th></tr><tr><td>https://ssl-images-amazon.com</td><td>508</td></tr><tr><td>https://sohu.com</td><td>332</td></tr><tr><td>https://doubleclick.net</td><td>271</td></tr><tr><td>https://msocdn.com</td><td>255</td></tr><tr><td>https://alicdn.com</td><td>243</td></tr><tr><td>https://pstatic.net</td><td>219</td></tr><tr><td>https://cloudfront.net</td><td>202</td></tr><tr><td>https://pinimg.com</td><td>200</td></tr><tr><td>https://dropboxstatic.com</td><td>189</td></tr><tr><td>https://google.com</td><td>181</td></tr></table>| <table> <tr><th>Domain</th><th>HTTP Requests</th></tr><tr><td>https://ssl-images-amazon.com</td><td>481</td></tr><tr><td>https://msocdn.com</td><td>255</td></tr><tr><td>https://pstatic.net</td><td>206</td></tr><tr><td>https://cloudfront.net</td><td>198</td></tr><tr><td>https://pinimg.com</td><td>195</td></tr><tr><td>https://alicdn.com</td><td>193</td></tr><tr><td>https://dropboxstatic.com</td><td>189</td></tr><tr><td>https://sinaimg.cn</td><td>156</td></tr><tr><td>https://qhimg.com</td><td>154</td></tr><tr><td>https://awsstatic.com</td><td>145</td></tr></table>|


## Third-Party Cookies Requests
![cookies.png](/cookies.png)


### Top-10 Third Party Domains (Cookies Requests)
|Vanilla|Adblock|
|--|--|
|<table> <tr><th>Domain</th><th>HTTP Requests</th></tr><tr><td>https://forbesimg.com/td><td>6694</td></tr><tr><td>https://media.net</td><td>2272</td></tr><tr><td>https://wsimg.com</td><td>1985</td></tr><tr><td>https://youtube.com</td><td>1483</td></tr><tr><td>https://google-analytics.com</td><td>1354</td></tr><tr><td>https://alicdn.com</td><td>1290</td></tr><tr><td>https://adobedtm.com</td><td>886</td></tr><tr><td>https://itc.cn</td><td>844</td></tr><tr><td>https://doubleclick.net</td><td>756</td></tr><tr><td>https://nytimes.com</td><td>738</td></tr></table>| <table> <tr><th>Domain</th><th>HTTP Requests</th></tr><tr><td>https://forbesimg.com</td><td>4996</td></tr><tr><td>https://wsimg.com</td><td>2597</td></tr><tr><td>https://youtube.com</td><td>1639</td></tr><tr><td>https://alicdn.com</td><td>1021</td></tr><tr><td>https://itc.cn</td><td>773</td></tr><tr><td>https://nytimes.com</td><td>599</td></tr><tr><td>https://cnn.com</td><td>507</td></tr><tr><td>https://awsstatic.com</td><td>498</td></tr><tr><td>https://segment.com</td><td>484</td></tr><tr><td>https://guim.co.uk</td><td>400</td></tr></table>|


## Third-Party Javascript API Requests
![js.png](/js.png)


### Top-10 Third Party Domains (Javascript API Requests)
|Vanilla|Adblock|
|--|--|
|<table> <tr><th>Domain</th><th>HTTP Requests</th></tr><tr><td>https://ssl-images-amazon.com</td><td>508</td></tr><tr><td>https://sohu.com</td><td>332</td></tr><tr><td>https://doubleclick.net</td><td>271</td></tr><tr><td>https://msocdn.com</td><td>255</td></tr><tr><td>https://alicdn.com</td><td>243</td></tr><tr><td>https://pstatic.net</td><td>219</td></tr><tr><td>https://cloudfront.net</td><td>202</td></tr><tr><td>https://pinimg.com</td><td>200</td></tr><tr><td>https://dropboxstatic.com</td><td>189</td></tr><tr><td>https://google.com</td><td>181</td></tr></table>| <table> <tr><th>Domain</th><th>HTTP Requests</th></tr><tr><td>https://ssl-images-amazon.com</td><td>481</td></tr><tr><td>https://msocdn.com</td><td>255</td></tr><tr><td>https://pstatic.net</td><td>206</td></tr><tr><td>https://cloudfront.net</td><td>198</td></tr><tr><td>https://pinimg.com</td><td>195</td></tr><tr><td>https://alicdn.com</td><td>193</td></tr><tr><td>https://dropboxstatic.com</td><td>189</td></tr><tr><td>https://sinaimg.cn</td><td>156</td></tr><tr><td>https://qhimg.com</td><td>154</td></tr><tr><td>https://awsstatic.com</td><td>145</td></tr></table>|

