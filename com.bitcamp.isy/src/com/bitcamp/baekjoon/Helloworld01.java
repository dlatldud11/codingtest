package com.bitcamp.baekjoon;

import java.util.ArrayList;
import java.util.Scanner;


public class Helloworld01 {
	
    public static void main(String[] args){
       Scanner kb = new Scanner(System.in);
       
    	int n = kb.nextInt(); // 물품수
    	int k = kb.nextInt(); // 최대키로수
    	int value = 0;
    	class Thing { // 물건
    		int w;
    		int v;
			public int getW() {
				return w;
			}
			public void setW(int w) {
				this.w = w;
			}
			public int getV() {
				return v;
			}
			public void setV(int v) {
				this.v = v;
			}
		}
    	ArrayList<Thing> things = new ArrayList<Thing>();
    	for(int i=0; i<n;++i) {
    		Thing thing = new Thing();
    		int w = kb.nextInt();
    		int v = kb.nextInt();
    		thing.setW(w);
    		thing.setV(v);
    		things.add(thing);
    	}
    	for(Thing a : things) {
    		for(Thing b : things) {
    			if(a.getW() != b.getW()) {
    				if(a.getW()+b.getW() <= k) {
    					value = a.getV()+b.getV();
    				}
    			}
    		}
    	}
    	System.out.println(value);
    	
    	
    }
    }

	
