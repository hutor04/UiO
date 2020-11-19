; 1.A
(cons 42 11)
;     +-------+-------+
;     |       |       |
;+--->+   +   |   +----->11
;     |   |   |       |
;     +-------+-------+
;         |
;         v
;         42


; 1.B
(cons 42 '())
;     +-------+-------+
;     |       |      X|
;+--->+   +   |   X   |
;     |   |   |X      |
;     +---------------+
;         |
;         v
;         42


; 1.C
(list 42 11)
;     +-------+-------+  +-------+-------+
;     |       |       |  |       |      X|
;+--->+   +   |   +----->+   +   |   X   |
;     |   |   |       |  |   |   |X      |
;     +-------+-------+  +---------------+
;         |                  |
;         v                  v
;         42                 11


; 1. D
 '(42 (11 12))
;                                       (11 12)
;                                          +
;                                          |
;                                          v
;            +-------+-------+     +---+---+-------+   +-------+------+
;(42 (11 22))|       |       |     |       |       |   |       |     X|
;       +--->+   +   |   +-------->+   +   |   +------>+   +   |   X  |
;            |   |   |       |     |   |   |       |   |   |   |X     |
;            +-------+-------+     +-------+-------+   +--------------+
;                |                     |                   |
;                v                     v                   v
;                42                    11                  12


; 1. E
(define foo '(1 2 3))
(cons foo foo)
;                 +------+------+    +------+------+     +------+------+
;          (1 2 3)|      |      |    |      |      |     |      |     X|
;         +------>+   +  |   +------>+   +  |  +-------->+   +  |  X   |
;         |       |   |  |      |    |   |  |      |     |   |  |X     |
;      +-----+    +------+------+    +------+------+     +-------------+
;      |  +  |        |                  |                   |
;      |     |        v                  v                   v
;+---->------+        1                  2                   3
;      |     |
;      |  +  |    +------+------+    +------+------+     +------+------+
;      +-----+    |      |      |    |      |      |     |      |     X|
;         |       |   +  |   +------>+   +  |  +-------->+   +  |  X   |
;         +------>+   |  |      |    |   |  |      |     |   |  |X     |
;          (1 2 3)+------+------+    +------+------+     +-------------+
;                     |                  |                   |
;                     v                  v                   v
;                     1                  2                   3

; 1. F
(car (cdr (list 0 42 #t 'bar)))

; 1.G
(car
 (cdr
  (car
   (list (list 0 42) (list #t 'bar)))))

; 1. H
(car
 (car
  (cdr
   (list (list 0) (list 42 #t) (list 'bar)))))


; 1. I
(cons
     (cons 0 42)
     (cons (cons #t 'bar) '()))

(list (list 0 42) (list #t 'bar))


; 2. A
(define (length2 items)
  (define (iter counter itms)
    (if (null? itms)
        counter
        (iter (+ counter 1) (cdr itms))))
  (iter 0 items))

"Test 2.A"
"4 expectes"
(length2 (list 1 2 3 4))
"0 Expected"
(length2 (list 1 2 3 4))

; 2. B
(define (rev-list input)
  (define (rev-list-iter in out)
    (if (null? in)
        out
    (rev-list-iter (cdr in)
                   (cons (car in) out))
    ))
  (rev-list-iter input '()))

"Test 2.B"
"(4 3 2 1) expected"
(rev-list (list 1 2 3 4))

; I am using list copy with tail recursion, since the side effect of this
; procedure is that list gets inversed.

; 2. C
(define (all? predicate input)
  (cond ((null? input) #t)
        ((predicate (car input)) (all? predicate (cdr input)))
        (else #f)
        ))

(define (more-than-null item)
  (if (< 0 item)
      #t
      #f))
"Testing 2. C"
"Predicate: more-than-null; Input:(1 2 3 4); True expected"
(all? more-than-null '(1 2 3 4))

"Predicate: more-than-null; Input:(1 2 -3 4); False expected"
(all? more-than-null '(1 2 3 4))

"Predicate: (lambda (x) (< x 10)); Input:(1 2 3 4); True expected "
(all? (lambda (x) (< x 10)) '(1 2 3 4))

"Predicate: (lambda (x) (< x 10)); Input:(1 2 3 50); False expected "
(all? (lambda (x) (< x 10)) '(1 2 3 50))

 ; 2. D
 (define (nth position input)
  (define (nth-iter counter items)
    (if (= position counter)
        (car items)
        (nth-iter (+ counter 1) (cdr items))
        ))
  (nth-iter 0 input))

"Test 2. D"
"12 Expected"
 (nth 2 '(47 11 12 13))

 ; 2. E
 (define (where item input)
  (define (where-iter counter input)
    (cond
      ((null? input) #f)
      ((equal? item (car input)) counter)
      (else (where-iter (+ counter 1) (cdr input)))
      
  )
  )
  (where-iter 0 input))
"Test 2. E"
"Input 3 and (1 2 3 4). Expected result 2."
(where 3 '(1 2 3 4))

"Input 10 and (1 2 3 4). Expected result #f."
(where 10 '(1 2 3 4))

; 2. F
; Returns empty list if either of the lists in initially empty.
(define (map2 proc items-1 items-2)
  (if (or (null? items-1) (null? items-2))
      '()
      (cons (proc (car items-1) (car items-2))
            (map2 proc (cdr items-1) (cdr items-2)))))

"Test 2.F"
"Input: + (1 2 3 4) (3 4 5). Expected (4 6 8)"
 (map2 + '(1 2 3 4) '(3 4 5))

 ; 2. G
 "Lambda that calculates average. Input: (1 2 3 4) (3 4 5). Expected value (2 3 4)."
  (map2 (lambda (x y) (/ (+ x y) 2)) '(1 2 3 4) '(3 4 5))

; 2. H
(define (both? proc)
  (lambda (x y)
    (if (and (proc x) (proc y))
     #t
     #f))
  )

"Testing 2.H"
"Input even? 2 4. Expected #t"
((both? even?) 2 4)

"Input even? 2 5. Expected #f"
((both? even?) 2 5)

"Input to map2. Expected (#f #t #f)"
(map2 (both? even?) '(1 2 3) '(3 4 5))

; 2. I
(define (self proc)
  (lambda (x) (proc x x))
  )

"Testing 2. I"

"10 Expected"
((self +) 5)

"9 Expected"
((self *) 3)

"#<procedure> Expected"
(self +)

"(hello hello) expected"
((self list) "hello")