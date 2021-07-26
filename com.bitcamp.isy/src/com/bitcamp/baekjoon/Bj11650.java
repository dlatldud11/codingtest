package com.bitcamp.baekjoon;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Bj11650 {
	
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int num = scanner.nextInt();
		int[][] numbers = new int[num][2]; // 2차원 배열 생성
		scanner.nextLine();
		for(int i=0; i<num;i++) {
			String a = scanner.nextLine();
			String[] number = a.split(" ");
//			System.out.println("첫번째:"+number[0]+"두번째:"+number[1]);
			numbers[i][0] = Integer.parseInt(number[0]);
			numbers[i][1] = Integer.parseInt(number[1]); // 받은 번호를 배열에 넣기
		}
		
	Arrays.sort(numbers,new Comparator<int[]>() {

		@Override
		public int compare(int[] o1, int[] o2) {
			if(o1[0] == o2[0]) {
				return o1[1] - o2[1];
			}else {
				return o1[0] - o2[0];
			}
		}
	});
	
	for(int i=0; i<numbers.length; i++) {
		System.out.println(numbers[i][0]+" "+numbers[i][1]);
	}
	scanner.close();
	}
	
}
