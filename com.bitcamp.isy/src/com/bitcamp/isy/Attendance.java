package com.bitcamp.isy;



public class Attendance {
	
	private String index;
	private String id;
	private String mon;
	private String tue;
	private String wen;
	private String thu;
	private String fri;
	private String sat;
	private String sun;
	
	public Attendance() {
		String o = "결석";
		this.setMon(o);
		this.setTue(o);
		this.setWen(o);
		this.setThu(o);
		this.setFri(o);
		this.setSat(o);
		this.setSun(o);
	}
	
	
	

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getMon() {
		return mon;
	}
	public void setMon(String mon) {
		this.mon = mon;
	}
	public String getTue() {
		return tue;
	}
	public void setTue(String tue) {
		this.tue = tue;
	}
	public String getWen() {
		return wen;
	}
	public void setWen(String wen) {
		this.wen = wen;
	}
	public String getThu() {
		return thu;
	}
	public void setThu(String thu) {
		this.thu = thu;
	}
	public String getFri() {
		return fri;
	}
	public void setFri(String fri) {
		this.fri = fri;
	}
	public String getSat() {
		return sat;
	}
	public void setSat(String sat) {
		this.sat = sat;
	}
	public String getSun() {
		return sun;
	}
	public void setSun(String sun) {
		this.sun = sun;
	}
	
	public String toString() {
		return " "+id+"\t"+mon+"\t"+tue+"\t"+wen+"\t"+thu+"\t"+fri+"\t"+sat+"\t"+sun;
	}
	
	public String toString2() {
		return " "+mon+"\t"+tue+"\t"+wen+"\t"+thu+"\t"+fri+"\t"+sat+"\t"+sun;
	}




	public void add(Attendance att) {
		// TODO Auto-generated method stub
		
	}
	
	
}
