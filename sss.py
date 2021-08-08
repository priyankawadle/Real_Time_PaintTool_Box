
include<opencv\cv.h>
include<opencv\highgui.h>
include<opencv2\imgproc\imgproc.hpp>
include<stdio.h>
include<conio.h>
include"bloborig.h"

int main()
{
	IplImage* img;
	int tlX,tlY,marea=2000,flag=0,px=0,py=0;
	CvScalar color=cvScalar(0,0,255);
	CvCapture* cam=cvCaptureFromCAM(0);
	img=cvQueryFrame(cam);
    CvSize s=cvGetSize(img);
	cvSetCaptureProperty(cam,CV_CAP_PROP_FPS,30);
	cvSetCaptureProperty(cam,CV_CAP_PROP_FRAME_WIDTH,640);
	cvSetCaptureProperty(cam,CV_CAP_PROP_FRAME_HEIGHT,480);
	cvNamedWindow("Out",CV_WINDOW_AUTOSIZE);
	cvNamedWindow("Bin",CV_WINDOW_AUTOSIZE);
	IplImage* paint = cvCreateImage(s,IPL_DEPTH_8U,3);
	cvSet(paint,cvScalar(255,255,255));
	cvNamedWindow("yeahh",CV_WINDOW_AUTOSIZE);
	rectfill(paint,cvPoint(5,1),cvPoint(100,65),cvScalar(122,122,122));
	rectfill(paint,cvPoint(150,1),cvPoint(250,65),cvScalar(0,0,255));
	rectfill(paint,cvPoint(300,1),cvPoint(400,65),cvScalar(0,255,0));
	rectfill(paint,cvPoint(450,1),cvPoint(550,65),cvScalar(255,0,0));
	CvFont f;
	cvInitFont(&f,1,1,1);
	cvPutText(paint,"ERASE ALL",cvPoint(9,33),&f,cvScalar(255,255,255));
	cvPutText(paint,"RED",cvPoint(180,33),&f,cvScalar(0,0,0));
	cvPutText(paint,"GREEN",cvPoint(330,33),&f,cvScalar(0,0,0));
	cvPutText(paint,"BLUE",cvPoint(480,33),&f,cvScalar(0,0,0));
	cvPutText(paint,"ADD TEXT",cvPoint(555,33),&f,cvScalar(0,0,0));
	cvShowImage("yeahh",paint);
	cvWaitKey(0);
	char ch[20];
	while(1)
	{
		img=cvQueryFrame(cam);
		cvFlip(img,img,1);
		if(img!=NULL && img->nChannels==3)
		{  IplImage* gray = cvCreateImage(cvGetSize(img),IPL_DEPTH_8U,1);
		 IplImage* red = cvCreateImage(cvGetSize(img),IPL_DEPTH_8U,1);
		  IplImage* blue = cvCreateImage(cvGetSize(img),IPL_DEPTH_8U,1);
		  cvSplit(img,blue,NULL,NULL,NULL);
		  cvSplit(img,NULL,NULL,red,NULL);
		  cvSub(red,blue,gray);
		  cvThreshold(gray,gray,55,255,CV_THRESH_BINARY);
		  cvSmooth(gray,gray,CV_GAUSSIAN,7,7);
		  cvThreshold(gray,gray,220,255,CV_THRESH_BINARY);
		  tlX=gray->width;
		  tlY=gray->height;
		  int* label=new int[tlX*tlY];
long coun=labelxy(gray,label);  // labelling the image
long* sx=new long[coun];
long* sy=new long[coun];
long* c=new long[coun];
int max=centroid(gray,label,coun,sx,sy,c);  // centroid of max area blob
if(marea<c[max])
{
	if(sy[max]>65)
	{
		if(flag==0)
		{
			if(px==0 && py==0)
		cvLine(paint,cvPoint(sx[max],sy[max]),cvPoint(sx[max],sy[max]),color,4);
			else
		cvLine(paint,cvPoint(px,py),cvPoint(sx[max],sy[max]),color,4);
		px=sx[max];
		py=sy[max];
		}
		else
		{
			flag=0;
			cvPutText(paint,ch,cvPoint(sx[max],sy[max]),&f,cvScalar(0,0,0));
			//for(int g=0;g<19;g++)
				//ch[g]=' ';
		}
	}
	else
	{
		if(sx[max]<100 && sx[max]>5)
			rectfill(paint,cvPoint(0,66),cvPoint(639,439),cvScalar(255,255,255));
		if(sx[max]<250 && sx[max]>150)
			color=cvScalar(0,0,255);
		if(sx[max]<400 && sx[max]>300)
			color=cvScalar(0,255,0);
		if(sx[max]<550 && sx[max]>450)
			color=cvScalar(255,0,0);
		if(sx[max]>551)
		{
			flag++;
			if(flag!=2)
			{printf("enter your string:\n");
			scanf("%s",&ch);
			printf("Now press to the location you want to insert it \n");
			}
			
		}
	}
}
		cvShowImage("yeahh",paint);
		cvShowImage("Out",img);
		cvShowImage("Bin",gray);
		cvReleaseImage(&red);
		cvReleaseImage(&blue);
		cvReleaseImage(&gray);
		delete label;
		}
		//cvReleaseImage(&img);
		if(cvWaitKey(1)==32) break;
	}

	cvReleaseCapture(&cam);
	cvReleaseImage(&paint);
		cvDestroyWindow("yeahh");
	cvDestroyWindow("Out");
		cvDestroyWindow("Bin");
	return 0;
}
paint1.cpp
Displaying paint1.cpp.
