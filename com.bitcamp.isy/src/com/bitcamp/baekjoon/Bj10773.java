package com.bitcamp.baekjoon;

import java.util.Scanner;
import java.util.Stack;

public class Bj10773 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		Stack<Integer> stack = new Stack<>();
		int a = scanner.nextInt(); scanner.nextLine();
		int answer = 0;
		for(int i=0; i<a; i++) {
			int num = scanner.nextInt();
			if(num == 0) {
				stack.pop();
			}else {
				stack.push(num);
			}
		}
		while(!stack.empty()) {
			answer += stack.peek();
			stack.pop();
		}
		System.out.println(answer);
		scanner.close();
	}
}
