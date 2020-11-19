; Task 1
; General comments:
; To evaluate the combination
; 1. Evaluate the subexpressions of the combination.
; 2. Apply the procedure that is the value of the leftmost subexpression
; to the arguments that are the values of the other subexpressions.

(* (+ 4 2) 5)
; (+ 4 2) evaluates to 6
; (* 6 5) evaluates to 30

; (* (+ 4 2) (5))
; (+ 4 2) evaluates to 6
; We get error
; Left most subexpression must be the procedure that can be applied to
; the arguments. 5 is not a procedure that can be applied

;(* (4 + 2) 5)
; We get error
; Left most subexpression must be the procedure that can be applied to
; the arguments. 4 is not a procedure that can be applied

(define bar (/ 44 2))
; define associates the first symbol bar with the value to which evaluates (/ 44 2)
; that is 22
bar
; prints 22

(- bar 11)
; bar evaluates to 22
; (- 22 11) evaluates to 11

(/ (* bar 3 4 1) bar)
; bar evaluates to 22
; (* 22 3 4 1) evaluates to 264
; bar evaluates to 22
; (/ 264 22) evaluates to 12

; Task 2.A
(or (= 1 2)
    "paff!"
    "piff!"
    (zero? (1 - 1)))
; Evaluates to "paff!"
; The interpreter evaluates the expressions one at a time, in left-to-right order.
; If any expression evaluates to a true value, that value is returned as the value
; of the or expression, and the rest of the expressions are not evaluated.
; (= 1 2) evaluates to false, "paff!" evaluates to true and is returned.
; (1 - 1) must be in prefix notation (- 1 1), but the interpreter does not reach
; it, thus it is not evaluated.

(and (= 1 2)
     "paff!"
     "piff!"
     (zero? (1 - 1)))
; evaluates to #f, i.e. false
; The interpreter evaluates the expressions one at a time, in left-to-right order.
; If any expression evaluates to false, the value of and expression is false, and
; the rest of the expressions are not evaluated.
; (= 1 2) evaluates to false, false is returned.
; (1 - 1) must be in prefix notation (- 1 1), but the interpreter does not reach
; it, thus it is not evaluated.

(if (positive? 42)
    "poff!"
    (i-am-undefined))
; evaluates to "poff!"
; To evaluate an if expression, the interpreter starts by evaluating the predicate
; part. If the predicate evaluates to a true value, the interpreter evaluates the consequent
; and returns its value. Otherwise it evaluates the alternative and returns its value.
; (positive? 42) evaluates to true, "poff!" is returned. (i-am-undefined) is never reached
; thus it does not raise an error.

; and, or, if are special forms because the subexpressions are not necessarily evaluated.

; Task 2.B
; with if
(define (sign x)
  (if (< x 0)
      -1
      (if (= x 0)
          0
          1)))
"Test task 2.B"
"Test with if"
(sign 10)
(sign 0)
(sign -10)

; with cond
(define (sign x)
  (cond ((< x 0) -1)
        ((= x 0) 0)
        ((> x 0) 1)))

"Test with cond"
(sign 10)
(sign 0)
(sign -10)

; Task 2.C

(define (sign x)
  (or (and (< x 0)
       -1)
      (and (= x 0)
        0)
      (and (> x 0)
         1)
      ))

"Test task 2.C"
"Test with and or"
(sign 10)
(sign 0)
(sign -10)

; Task 3.A
(define (add1 x)
  (+ x 1))

"Test task 3.A"
"Test add1 101 expected"
(add1 100)


(define (sub1 x)
  (- x 1))

"Test sub1 99 expected"
(sub1 100)

; Task 3.B
(define (plus x y)
  (cond ((zero? x) y)
        ((zero? y) x)
        (else (plus (sub1 x) (add1 y)))
        )
  )

"Test task 3.B"
"Test plus: sum of zeroes"
(plus 0 0)

"Test plus: sum of 5 and 0"
(plus 5 0)

"Test plus: sum of 0 and 6"
(plus 0 6)

"Test plus: sum of 5 and 6"
(plus 5 6)

; Task 3.C
; The procedure defined in task 3.B.is defined recursively, since in the definition the procedure
; refers to itselft, however the procedure is generating iterative process. The state of the process
; may be summarized at any time by the state of two variable x and y, where x acts like a counter
; and shows how many iterations we should go through to get the final result.
; The procedure below gives rize to the recursive process, the interpreter have to keep track of the
; operations to carried out later on.
(define (plus x y)
  (if (zero? x)
      y
      (add1 (plus (sub1 x) y))))

"Test task 3.C"
"Test plus: sum of zeroes"
(plus 0 0)

"Test plus: sum of 5 and 0"
(plus 5 0)

"Test plus: sum of 0 and 6"
(plus 0 6)

"Test plus: sum of 5 and 6"
(plus 5 6)

; Task 3.D
; It was not necessary to pass b and n explicitly to the enclosed power-iter procedure.
; Instead we allow them to be free variables in the definition of the procedure
; power-iter. b and n get their values from the enclosing procedure. I.e. we are using lexical
; scoping.
(define (power-close-to b n)
  (define (power-iter e)
    (if (> (expt b e) n)
        e
        (power-iter (+ 1 e)))
    )
  (power-iter 1))

"Test task 3.D"
(power-close-to 2 8)

; Task 3.E
; It is not possible to simplify the enclosed function fib-iter when using the block
; structure. Values of a, b, and count change from iteration to iteration and
; reflect the state of the program.