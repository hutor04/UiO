.data
var1: .quad 60
var2: .quad 3600

	.globl hms_to_sec
# Omformer et klokkeslett (angitt i timer, minutter og sekunder) til
# antall sekunder.
	
hms_to_sec:

	# Legg inn kode for funksjonen her:
	imulq var2,%rdi
	imulq var1,%rsi
	movq %rdi,%rax
	addq %rsi,%rax
	addq %rdx,%rax	
	ret
	

	.globl	sec_to_h
# Gitt et tidspunkt (angitt som sekunder siden midnatt), finn timen.
	
sec_to_h:

	# Legg inn kode for funksjonen her:
	movq %rdi,%rax
	cqo
	idivq var2	
	ret

	
	.globl	sec_to_s
# Gitt et tidspunkt (angitt som sekunder siden midnatt), finn sekundet.
	
sec_to_s:

	# Legg inn kode for funksjonen her:
	call sec_to_h
	imulq var2,%rax
	movq %rax,%r8
	call sec_to_m
	imulq var1,%rax
	subq %rax,%rdi
	subq %r8,%rdi
	movq %rdi,%rax
	ret

	
	.globl	sec_to_m
# Gitt et tidspunkt (angitt som sekunder siden midnatt), finn minuttet.
	
sec_to_m:

	# Legg inn kode for funksjonen her:
	movq %rdi,%r9
	call sec_to_h
	imulq var2,%rax
	subq %rax,%r9
	movq %r9,%rax
	cqo
	idivq var1
	ret
