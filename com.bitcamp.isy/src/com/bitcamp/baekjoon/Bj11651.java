package com.bitcamp.baekjoon;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Bj11651 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int a = scanner.nextInt(); scanner.nextLine();
		int[][] numbers = new int[a][2]; // 좌표를 담을 배열
		for(int i=0; i<a; i++) {
			String s = scanner.nextLine(); // 한줄 읽음
		
			String[] number = s.split(" ");
			numbers[i][0] = Integer.parseInt(number[0]);
			numbers[i][1] = Integer.parseInt(number[1]);
		}
		Arrays.sort(numbers,new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
				if(o1[1] == o2[1]) {
					return o1[0] - o2[0];
				}else {
					return o1[1] - o2[1];
				}
			}
		});
		for(int i=0; i<numbers.length; i++) {
			System.out.println(numbers[i][0]+" "+numbers[i][1]);
		}
		
	}
}
