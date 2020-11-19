	.globl hms_to_sec
# Omformer et klokkeslett (angitt i timer, minutter og sekunder) til
# antall sekunder.
	
hms_to_sec:

	# Legg inn kode for funksjonen her:
	movq %rdi,%rax
	imulq $3600,%rax
	movq %rsi,%r8
	imulq $60,%r8
	addq %r8,%rax
	addq %rdx,%rax	
	ret
	

	.globl	sec_to_h
# Gitt et tidspunkt (angitt som sekunder siden midnatt), finn timen.
	
sec_to_h:

	# Legg inn kode for funksjonen her:
	movq %rdi,%rax
	movq $3600,%r8
	cqo
	idivq %r8	
	ret

	
	.globl	sec_to_s
# Gitt et tidspunkt (angitt som sekunder siden midnatt), finn sekundet.
	
sec_to_s:

	# Legg inn kode for funksjonen her:
	movq %rdi,%rax
	movq %rdi,%r9
	movq $3600,%r8
	cqo
	idivq %r8
	imulq $3600,%rax
	movq %rax,%r10
	subq %rax,%r9
	movq %r9,%rax
	movq $60,%r8
	cqo
	idivq %r8
	imulq $60,%rax
	subq %r10,%rdi
	subq %rax,%rdi
	movq %rdi,%rax
	ret

	
	.globl	sec_to_m
# Gitt et tidspunkt (angitt som sekunder siden midnatt), finn minuttet.
	
sec_to_m:

	# Legg inn kode for funksjonen her:
	movq %rdi,%rax
        movq %rdi,%r9
        movq $3600,%r8
        cqo
        idivq %r8
        imulq $3600,%rax
        subq %rax,%r9 	
	movq %r9,%rax
	movq $60,%r8
	cqo
	idivq %r8
	ret
