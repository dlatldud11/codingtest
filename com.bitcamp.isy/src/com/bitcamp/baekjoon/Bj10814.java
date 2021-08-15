package com.bitcamp.baekjoon;

import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class Bj10814 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int a = scanner.nextInt(); scanner.nextLine();
		TreeMap<Integer, String> map = new TreeMap<>();
		for(int i=0; i<a; i++) {
			String str = scanner.nextLine();
//			System.out.println("입력문자열"+str);
			String[] strarr = str.split(" ");
//			System.out.println("잘린문자열"+strarr[0]+"/"+strarr[1]);
			if(map.containsKey(Integer.parseInt(strarr[0]))){
				map.put(Integer.parseInt(strarr[0]),map.get(Integer.parseInt(strarr[0]))+"/"+strarr[1]);
			}else {
				map.put(Integer.parseInt(strarr[0]), strarr[1]);
			}
		}
		for(Map.Entry<Integer,String> entry: map.entrySet()) {
			Integer key = entry.getKey();
			String[] value = entry.getValue().split("/");
			for(int i=0; i<value.length; i++) {
				System.out.println(key+" "+value[i]);
			}
		}
		scanner.close();
	}
}
