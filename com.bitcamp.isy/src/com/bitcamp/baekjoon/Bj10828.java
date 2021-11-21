package com.bitcamp.baekjoon;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Bj10828 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	int num = Integer.parseInt(br.readLine());
	Stack<Integer> stack = new Stack<>(); //int형 스택 선언
	for(int i=0; i<num; i++) {
		String str = br.readLine(); //문장 가져오기
		String[] s = str.split(" ");
		//System.out.println(i+"번");
		switch(s[0]){
		case "push": stack.push(Integer.parseInt(s[1]));
			break;
		case "pop": 
			if(stack.empty()) { // 비어있으
				System.out.println("-1");
			}else {
				System.out.println(stack.peek());
				stack.pop();
			}
			break;
		case "size": System.out.println(stack.size());
			break;
		case "empty": 
			if(stack.empty()) { // 비어있으
				System.out.println("1");
			}else {
				System.out.println("0");
			}
			break;
		case "top":
			if(stack.empty()) { // 비어있으
				System.out.println("-1");
			}else {
				System.out.println(stack.peek());
			}
			break;
		}
	}
	br.close();	
}
}
