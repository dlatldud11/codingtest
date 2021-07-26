package com.bitcamp.isy;

import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.io.BufferedReader;
import java.io.IOException;
import org.json.simple.JSONObject; // JSON객체 생성
import org.json.simple.parser.JSONParser; // JSON객체 파싱
import org.json.simple.parser.ParseException; // 예외처리
 
public class test {
    public static void main(String[] args) throws IOException, ParseException {
        StringBuilder urlBuilder = new StringBuilder("http://openapi.seoul.go.kr:8088" ); /*URL*/
        urlBuilder.append("/5876546e6a6e6e6d313035734d716c50"); /*Service Key*/
        urlBuilder.append("/" +  URLEncoder.encode("json", "UTF-8")); /*한 페이지 결과 수*/
        urlBuilder.append("/" +  URLEncoder.encode("LOCALDATA_072404", "UTF-8")); /*페이지 번호*/
        urlBuilder.append("/" +  URLEncoder.encode("1", "UTF-8")); /*측정소 이름*/
        urlBuilder.append("/" +  URLEncoder.encode("5", "UTF-8") + "/"); /*요청 데이터기간 (하루 : DAILY, 한달 : MONTH, 3달 : 3MONTH)*/
        URL url = new URL(urlBuilder.toString());
        System.out.println(urlBuilder.toString());
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        conn.setRequestProperty("Content-type", "application/json");
        System.out.println("Response code: " + conn.getResponseCode());
        BufferedReader rd;
        if(conn.getResponseCode() >= 200 && conn.getResponseCode() <= 300) {
            rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        } else {
            rd = new BufferedReader(new InputStreamReader(conn.getErrorStream()));
        }
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = rd.readLine()) != null) {
            sb.append(line);
        }
        rd.close();
        conn.disconnect();
        System.out.println(sb.toString());
        
        JSONParser jsonParser = new JSONParser();

        JSONObject jsonObject = (JSONObject) jsonParser.parse(sb.toString());
        System.out.print("name : " + jsonObject.get("BPLCNM"));
    }
}
