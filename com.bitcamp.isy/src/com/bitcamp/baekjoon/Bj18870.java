package com.bitcamp.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class Bj18870 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		ArrayList<Integer> arr = new ArrayList<Integer>();
			
		String[] strarr = br.readLine().split(" "); // 한번에 다 받음
		int[] nums = Arrays.stream(strarr).mapToInt(Integer::parseInt).toArray();
		for(int i=0; i<a; i++) {
				arr.add(nums[i]); //나눈 숫자들을 넣어주기
		}
		Collections.sort(arr);
		Map<Integer,Integer> map = new HashMap<Integer,Integer>();
		int count = 0;
		for(int i=0; i<arr.size(); i++) {
			if(!map.containsKey(arr.get(i))) {
				map.put(arr.get(i),count++);
			}
		}
		
		for(int i=0; i<a; i++) {
			sb.append(map.get(nums[i])).append(" ");
		}
		System.out.println(sb.toString());
	}
}
