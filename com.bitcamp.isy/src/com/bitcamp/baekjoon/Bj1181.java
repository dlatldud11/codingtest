package com.bitcamp.baekjoon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class Bj1181 {
public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	int a = scanner.nextInt();
	ArrayList<String> arr = new ArrayList<String>();
	for(int i=0; i<a;i++) {
		String str = scanner.next();
		if(!arr.contains(str)) {
			arr.add(str);
		}
	}
	Collections.sort(arr,new Comparator<String>() {

		@Override
		public int compare(String o1, String o2) {
			if(o1.length() == o2.length()) {
				int num = 0;
				for(int i=0; i<o1.length(); i++) {
					if(o1.charAt(i) == o2.charAt(i)) {
//						System.out.println("같은글씨나옴"+i+"/"+num);
					}else {
						num = o1.charAt(i) - o2.charAt(i);
//						System.out.println("같은글씨안나옴"+i+"/"+num);
						break;
					}
				}
				return num;
			}else {
				return o1.length() - o2.length();
			}
		}
	});
	
	for(String b : arr) {
		System.out.println(b);
	}
	scanner.close();
}
}
