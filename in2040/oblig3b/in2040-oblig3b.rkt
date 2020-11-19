(load "evaluator.scm")
(set! the-global-environment (setup-environment))

; Task 1.A

; (define (foo cond else)
;   (cond ((= cond 2) 0)
;         (else (else cond))))

; (define cond 3)
; (define (else x) (/ x 2))
; (define (square x) (* x x))


; Case 1
; (foo 2 square) -> 0

; First, 'cond' and 'else' are detected and distinguished from variables
; by the evaluator using cond? and cond-clauses.
; Although 'cond' and 'else' are defined in the global environment they
; become local in 'foo'. Thus 'cond' is assigned to value 2. And 'else' refers
; to 'square'. This happens because the code runs in separate environment of
; the 'foo' procedure. 'cond' and 'else' are bound to the values the function
; was called with.

; Case 2
; (foo 4 square) -> 16

; Same explanation as in Case 1.

; Case 3
; (cond ((= cond 2) 0)
;       (else (else 4))) -> 2

; In this case 'cond' and 'else' have the values assigned in the global
; environment. Thus, 'cond' is 3 and 'else' evaluates to lamda (x) (/ x 2).

; Task 2.A

(define primitive-procedures
  (list (list 'car car)
        (list 'cdr cdr)
        (list 'cons cons)
        (list 'null? null?)
        (list 'not not)
        (list '+ +)
        (list '- -)
        (list '* *)
        (list '/ /)
        (list '= =)
        (list 'eq? eq?)
        (list 'equal? equal?)
        (list 'display 
              (lambda (x) (display x) 'ok))
        (list 'newline 
              (lambda () (newline) 'ok))
; New primitive 1+
        (list '1+
              (lambda (x) (+ 1 x)))

; New primitive 1-        
        (list '1-
              (lambda (x) (- x 1)))
        ))

; Task 2.B

(define (install-primitive! name proc)
  (define-variable! name (list 'primitive proc) the-global-environment)
  (display name)
  (display " ")
  (display 'installed!))

"Testing 2.B"
(install-primitive! 'square (lambda (x) (* x x)))


; Task 3.A

; First, we add 'and' and 'or' to the list of special forms.
(define (special-form? exp)
  (cond ((quoted? exp) #t)
        ((assignment? exp) #t)
        ((definition? exp) #t)
        ((if? exp) #t)
        ((lambda? exp) #t)
        ((begin? exp) #t)
        ((cond? exp) #t)
        ((and? exp) #t) ; New entry for AND
        ((or? exp) #t)  ; New entry for OR
        (else #f)))


; Ipdating predicates and selectors that define syntax
(define (and? exp) (tagged-list? exp 'and))
(define (or? exp) (tagged-list? exp 'or))

; We update the evaluator of the special forms with new evaluation
; rules.
(define (eval-special-form exp env)
  (cond ((quoted? exp) (text-of-quotation exp))
        ((assignment? exp) (eval-assignment exp env))
        ((definition? exp) (eval-definition exp env))
        ((if? exp) (eval-if exp env))
        ((lambda? exp)
         (make-procedure (lambda-parameters exp)
                         (lambda-body exp)
                         env))
        ((begin? exp) 
         (eval-sequence (begin-actions exp) env))
        ((cond? exp) (mc-eval (cond->if exp) env))
        ((and? exp) (eval-and exp env)) ; New entry for ADD
        ((or? exp) (eval-or exp env)))) ; New entry for OR


; We then create procedures that evaluate the epxressions
; Evaluation of AND
(define (eval-and exp env)
  (if (null? (cdr exp))
      #t
      (if (false? (mc-eval (cadr exp) env))
          #f
          (eval-and (cons 'and (cddr exp)) env))))


; Evaluation of OR
(define (eval-or exp env)
  (if (null? (cdr exp))
      #f
      (if (true? (mc-eval (cadr exp) env))
          #t
          (eval-or (cons 'or (cddr exp)) env))))


; Task 3.B
; Rewrite the function eval-if
(define (eval-if exp env)  
  (if (else? exp)
      (mc-eval (if-alternative exp) env)

  ; Check predicate and check if 'then' keyword is in place
  (if (and (true? (mc-eval (if-predicate exp) env)) (then? exp))
      (mc-eval (if-consequent exp) env)
      ; Check if the next part of expression begins with elsif or if
      (if (or (elsif? (elsif-part exp)) (else? (elsif-part exp)))
          (eval-if (elsif-part exp) env)
          (display 'FAILED)))))

(define (if-consequent exp) (cadddr exp)) ; Updated caddr -> cadddr

(define (if-alternative exp) (cadr exp)) ; Updated

(define (elsif-part exp) (cddddr exp)) ; New procedure

; New procedures to handle keywords
(define (then? exp)
  (eq? 'then (caddr exp)))

(define (elsif? exp)
  (eq? 'elsif (car exp)))

(define (else? exp)
  (eq? 'else (car exp)))
  
; Task 3.C
; First, we add 'let' to the list of special forms.
(define (special-form? exp)
  (cond ((quoted? exp) #t)
        ((assignment? exp) #t)
        ((definition? exp) #t)
        ((if? exp) #t)
        ((lambda? exp) #t)
        ((begin? exp) #t)
        ((cond? exp) #t)
        ((and? exp) #t)
        ((or? exp) #t)
        ((let? exp) #t) ; New entry for LET
        (else #f)))

; Ipdating predicates and selectors that define syntax
(define (let? exp) (tagged-list? exp 'let))

; We update the evaluator of the special forms with new evaluation
; rules.
(define (eval-special-form exp env)
  (cond ((quoted? exp) (text-of-quotation exp))
        ((assignment? exp) (eval-assignment exp env))
        ((definition? exp) (eval-definition exp env))
        ((if? exp) (eval-if exp env))
        ((lambda? exp)
         (make-procedure (lambda-parameters exp)
                         (lambda-body exp)
                         env))
        ((begin? exp) 
         (eval-sequence (begin-actions exp) env))
        ((cond? exp) (mc-eval (cond->if exp) env))
        ((and? exp) (eval-and exp env))
        ((or? exp) (eval-or exp env))
        ((let? exp) (mc-eval (let->lambda exp) env)))) ; New entry for LET

; Procedures for the evaluation of LET
(define (let->lambda exp)
  (let ((parameters (cadr exp))
        (body (caddr exp)))
    (make-lambda parameters body)))

(define (make-lambda parameters body)
  (cons (list 'lambda (map car parameters) body) (map cadr parameters)))

; Task 3.D
; Check if syntax is ok
(define (check-assignment-syntax exp)
  (and (eq? '= (cadr exp)) (or (eq? 'and (cadddr exp)) (eq? 'in (cadddr exp)))))

; Read parameters
(define (read-parameters exp)
  (if (list? (car exp))
      '()
      (if (check-assignment-syntax exp)
          (cons (cons (car exp) (list (caddr exp)))
                (read-parameters (cddddr exp)))
          (display 'FAILED))
      ))

; Read Body
(define (read-body exp)
  (if (list? (car exp))
      (car exp)
      (if (check-assignment-syntax exp)
          (read-body (cddddr exp)))
      ))

; Procedures for the evaluation of LET
(define (let->lambda exp)
  (let ((parameters (read-parameters (cdr exp)))
        (body (read-body (cdr exp))))
    (make-lambda parameters body)))

(define (make-lambda parameters body)
  (cons (list 'lambda (map car parameters) body) (map cadr parameters)))