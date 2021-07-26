package com.bitcamp.baekjoon;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Bj2108 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		int a = scanner.nextInt();// 들어오는 갯수
		double first = 0.0; // 산술평균
		int[] thirdlist = new int[8001]; // 최빈값
		ArrayList<Double> list = new ArrayList<Double>();
		for(int i =0; i<a; i++ ) {
			double value = scanner.nextInt();
			list.add(value);
			// 1번째 평균 구하기
			first = first + value;
			int third = (int)value + 4000;
			thirdlist[third]++; // 자리수 올리기
		}
		//산술평균 출력하기
		System.out.println(String.format("%.0f",first/a)); // 소숫점 이하 첫째자리에서 반올림한 값..?
		//중앙값 출력하기
		Collections.sort(list);
		System.out.println(String.format("%.0f",list.get((a/2))));
		//최빈값 출력하기
		int test = 0;
		boolean check = false;
		int third = 0;
		ArrayList<Integer> thirdarr = new ArrayList<Integer>();
		for(int i=0; i<thirdlist.length;i++) {
			if(test<thirdlist[i]) {
				test = thirdlist[i];
				third = i;
			}else if(test != 0 && test == thirdlist[i]) {
				check = true; // 같은 값이 또 있으면 true로 하기
				test = thirdlist[i];
//				System.out.println("같은 값 또 있음 :"+thirdlist[i]+"/"+i);
			}
		}
		if(check) {
			for(int i = 0;i<thirdlist.length;i++) {
				if(test == thirdlist[i]) {
					thirdarr.add(i);
				}
			}
			Collections.sort(thirdarr);
			System.out.println("정렬 확인 :"+thirdarr.get(0)+"/"+thirdarr.get(1));
			third = thirdarr.get(1)-4000;
		}else {
//		System.out.println("몇나왔는지 체크:"+third);
		third = third - 4000;
		}
		System.out.println(third);
		//범위 출력
		System.out.println(String.format("%.0f",list.get(list.size()-1)-list.get(0)));
		scanner.close();
	}
}
