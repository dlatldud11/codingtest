package com.bitcamp.baekjoon;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Deque;
import java.util.LinkedList;

public class Bj18258 {
	public static void main(String[] args) throws IOException {
		Deque<Integer> deque = new LinkedList<>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int a = Integer.parseInt(br.readLine());
		for(int i=0; i<a; i++) {
			String str = br.readLine();
			if(str.contains("push")) {
				String[] strl = str.split(" ");
				deque.add(Integer.parseInt(strl[1]));
			}
			if(str.contains("pop")) {
				if(deque.peek() == null) {
					sb.append(-1).append("\n");
							
				}else {
					sb.append(deque.peek()).append("\n");
					deque.poll();
				}
			}
			if(str.contains("size")) {
				sb.append(deque.size()).append("\n");
			}
			if(str.contains("empty")) {
				if(deque.peek() == null) {
					sb.append(1).append("\n");
				}else {
					sb.append(0).append("\n");
				}
			}
			if(str.contains("front")) {
				if(deque.peek() == null) {
					sb.append(-1).append("\n");
				}else {
					sb.append(deque.peek()).append("\n");
				}
			}
			if(str.contains("back")) {
				if(deque.peek() == null) {
					sb.append(-1).append("\n");
				}else {
					sb.append(deque.peekLast()).append("\n");
				}
			}
		}
		System.out.println(sb);
	}
}
