package com.bitcamp.baekjoon;

public class Pg01 {
	public static void main(String[] args) {
		String[] test = {"1","2","3"};
		for(String bean : test) {
			if(bean.equals("1")) {
				bean = "";
			}
		}
		for(String bean : test) {
			System.out.println(bean);
		}
	}
}
