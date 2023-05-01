# I've divided decoding into Steps.
# So start by lines annotated with Step1, then Step 2, and so on.
16:	8960
24:	10184
40:	4864
80:	136
88:	256
96:	768
104:	4864
112:	8960
120:	-768
136:	-8
144:	8
152:	-1			# Step 2. This is for "i++", or "i = i+1"
				# Search where address 152 is used below
160:	1
168:	-4294967296
176:	4294967296
184:	-2147483648
192:	16
200:	-16
208:	-1999			# Step 1. This is the constant to initialize mark1
216:	-203			# Step 1. mark2
224:	-2023
240:	752
248:	751



8960:	768	768	[NEXT]	# source line 2, Step 1
8984:	208	768	[NEXT]	# source line 2
9008:	776	776	[NEXT]
9032:	784/i	784/i	[NEXT]	# Step 3. i <- 0
9056:	328	328	[NEXT]
9080:	784/i	328	[NEXT]	# Step 4. *328 <- -i
9104:	216	328	9248	# Compare *216 and *328
				# We know from data above *216 is -203.  This confirms
				# This is actually the loop stop condition.
				
				# if (-i) - (-203) <= 0, goto 9248
				# or equivalently
				# if  i >= 203, goto 9248

9128:	344	344	[NEXT]
9152:	784/i	344	[NEXT]
9176:	344	776	[NEXT]	# These three lines obviously subtracts -i from
				# 776, or equally adds i to 776.
				# so 776 is sum.

9200:	152	784/i	[NEXT]	# Step 2.  From this we deduce 784 is i.
				#	   mark i to all appearances of 784
#	-1	^ This must be "i"
				# Step 3.  i <- i + 1
9224:	360	360	9056
9248:	792	792	[NEXT]
9272:	224	792	[NEXT]	# source line 7, Step 1
9296:	256	256	[NEXT]	# source line 7
#  Step 1. Everything below is cleanup code, ignore.
9320:	232	256	[NEXT]
9344:	240	40	[NEXT]
9368:	416	416	[NEXT]
9392:	248	416	[NEXT]
9416:	408	408	[NEXT]
9440:	120	408	[NEXT]
9464:	384	384	[NEXT]
9488:	400	400	[NEXT]
9512:	9584	9584	[NEXT]
9536:	40	384	[NEXT]
9560:	384	9584	[NEXT]
9584:	0	400	[NEXT]
9608:	384	384	[NEXT]
9632:	9832	9832	[NEXT]
9656:	9800	9800	[NEXT]
9680:	9808	9808	[NEXT]
9704:	408	384	[NEXT]
9728:	384	9832	[NEXT]
9752:	384	9800	[NEXT]
9776:	384	9808	[NEXT]
9800:	0	0	[NEXT]
9824:	400	0	[NEXT]
9848:	136	408	[NEXT]
9872:	136	40	[NEXT]
9896:	136	416	9464
9920:	240	40	[NEXT]
9944:	144	40	[NEXT]
9968:	432	432	[NEXT]
9992:	448	448	[NEXT]
10016:	10088	10088	[NEXT]
10040:	40	432	[NEXT]
10064:	432	10088	[NEXT]
10088:	0	448	[NEXT]
10112:	10176	10176	[NEXT]
10136:	448	10176	[NEXT]
10160:	456	456	10176
