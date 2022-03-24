package com.bitcamp.baekjoon;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Bj11279 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());
		
		int num = scanner.nextInt();
		int answer = 0;
		for(int i = 0; i<num; i++) {
			int a = scanner.nextInt();
			if(a > 0) {
				// 우선순위 큐에 넣기
				pq.add(a);
			}else {
				// 우선순위 큐에서 삭제하기(출력하면서)
				if(pq.peek() != null) {
					answer = pq.poll(); 
				}else {
					answer = 0;
				}
				System.out.println(answer);
			}
		}
	}
}
