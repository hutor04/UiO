(load "huffman.rkt")
; Task 1. A

(define (p-cons x y)
  (lambda (proc) (proc x y)))

(define (p-car proc)
  (proc (lambda (x y) x)))

(define (p-cdr proc)
  (proc (lambda (x y) y)))

"Testing Task 1.A"
"Foo expected"
(p-car (p-cons "foo" "bar"))

"Bar expected"
(p-cdr (p-cons "foo" "bar"))

"Foo expected"
(p-car (p-cdr (p-cons "zoo" (p-cons "foo" "bar"))))

; Task 1.B

(define foo 42)

"Testing 1.B"
""

"different is expected"
((lambda (foo x)
   (if (= x foo)
       'same
       'different)) 5 foo)

"(towel (42 towel)) is expected"
((lambda (bar baz)
   ((lambda (bar foo)
      (list foo bar))
    (list bar baz) baz)) foo 'towel)

; Task 1.C
(define (infix-eval exp)
  (let ((operator (car (cdr exp)))
        (operand-1 (car exp))
        (operand-2 (car (cdr (cdr exp)))))
(operator operand-1 operand-2)))

"Testing 1.C"
(define foo (list 21 + 21))
(define baz (list 21 list 21))
(define bar (list 84 / 2))
(infix-eval foo)
(infix-eval baz)
(infix-eval bar)

; Task 1.D
; (define bah '(84 / 2))
; (infix-eval bah)
; application: not a procedure, expected a procedure that can be applied to
; arguments given: /
; / is evaluated not as a procedure but as a symbol.

; Task 2.A
; We need the original tree to run this part of code (decode-1 (cdr bits) tree),
; if decode-1 is not encapsulated this part of code will be applied to subtrees
; not an original tree on subsequent calls.

; Task 2.B
"Testing 2.B"
"(ninjas fight ninjas by night) is expected."

(define (decode-tail bits tree)
  (define (decode-1 bits current-branch result)
    (if (null? bits)
        result
        (let ((next-branch
               (choose-branch (car bits) current-branch)))
          (if (leaf? next-branch)
              (decode-1 (cdr bits) tree
                        (append result (list (symbol-leaf next-branch))))
              (decode-1 (cdr bits) next-branch result)))))
  (decode-1 bits tree '()))

(decode sample-code sample-tree)

; Task 2.C
; (decode sample-code sample-tree) returns the result
; (ninjas fight ninjas by night)

; Task 2.D

; Node Finfer
(define (find-node tree value path)
  (if (leaf? tree)
      (if (eq? value (car (symbols tree)))
          path
          '())
      (let ((left (left-branch tree))
            (right (right-branch tree)))
        (append (find-node left value (append path '(0)))
        (find-node right value (append path '(1)))))))

; Encoder
(define (encode input tree)
(define (encode-iter string tree code)
  (if (null? string)
      '()
      (append (find-node tree (car string) '())
              (encode-iter (cdr string) tree code))
      )
  )
  (encode-iter input tree '()))

"Testing Task 2.D"
"(ninjas fight ninjas) is expected"
(decode (encode '(ninjas fight ninjas) sample-tree) sample-tree)

; Task 2.E
(define (grow-huffman-tree-1 freqs)
  (if (null? (cdr freqs))
      freqs
  (let ((one (car freqs))
        (two (cadr freqs)))
          (grow-huffman-tree-1 (adjoin-set (make-code-tree one two)
                                          (cdr (cdr freqs)))))))

(define (grow-huffman-tree freqs)
  (car (grow-huffman-tree-1 (make-leaf-set freqs))
  ))

"Testing Task 2.E"
"(a b c) is expected"

(define freqs '((a 2) (b 5) (c 1) (d 3) (e 1) (f 3)))
(define codebook (grow-huffman-tree freqs))
(decode (encode '(a b c) codebook) codebook)

; Task 2.F
(define freqs-2 '((samurais 57) (ninjas 20) (fight 45) (night 12) (hide 3)
                  (in 2) (ambush 2) (defeat 1) (the 5) (sword 4) (by 12)
                  (assassin 1) (river 2) (forest 1) (wait 1) (poison 1)))

(define codebook-2 (grow-huffman-tree freqs-2))

; Counts elements in a list
(define (counter lst)
  (cond ((null? lst) 0)                 
        ((not (pair? lst)) 1)           
        (else (+ (counter (car lst)) 
                 (counter (cdr lst))))))

(define message '(ninjas fight ninjas fight ninjas ninjas fight samurais
                  samurais fight samurais fight ninjas ninjas fight by night))

(define encoded-msg (encode message codebook-2))
"Hvor mange bits bruker det på å kode meldingen?"
(define no-bits (counter encoded-msg))
no-bits
; 43

"Hva er den gjennomsnittlige lengden på hvert kodeord som brukes?"
(/ no-bits (counter message))
; 2.52

; Hva er det minste antall bits man ville trengt for å kode meldingen med
; en kode med fast lengde (fixed-length code) over det samme alfabetet?

; We need log2(n) in order to differentiate n symbols.
; There are 16 symbols in the alfabet. We need 4 bits to encode each symbol.
; There are 17 tokens in the message. Thus we need 68 bits to encode it.

; Task 2.G

(define (huffman-leaves-1 tree leaves)
  (if (null? tree)
      leaves
  (if (leaf? tree)
      (cons (list (symbol-leaf tree) (weight-leaf tree)) leaves)
      (let ((left (left-branch tree))
            (right (right-branch tree)))
        (append (huffman-leaves-1 left leaves)
        (huffman-leaves-1 right leaves))))))


(define (huffman-leaves tree)
  (huffman-leaves-1 tree '()))

"Testign Task 2.G"
"((ninjas 8) (fight 5) (night 1) (by 1)) is expected."
(huffman-leaves sample-tree)

; Task 2.F

; Reducer
(define (reduce fn list init)
  (if (null? list) init
      (fn (car list)
          (reduce fn (cdr list) init))))

(define (expected-codeword-length tree)

; Encode wrapper
(define (encode-one element)
  (encode (cons element '()) sample-tree))

;Extract leaves
(define freqs-leaves (make-leaf-set (huffman-leaves sample-tree)))
freqs-leaves
; Frequency of each token
(define freqs-weights (map weight-leaf freqs-leaves))

; Sum of all weights
(define freqs-sum-weights (reduce + freqs-weights 0))

; Devide by sum of weights
(define (divide-by-weight element)
  (/ element  freqs-sum-weights))

; Get each symbol
(define freqs-symblos (map symbol-leaf freqs-leaves))

; Probability of each symbols
(define freqs-prob (map divide-by-weight freqs-weights))
freqs-prob
; Get bits for each symbol
(define freqs-bits (map encode-one freqs-symblos))

; Length of code
(define freqs-bits-length (map counter freqs-bits))

; Sum of probabilities multiplied by code length
(reduce + (map * freqs-prob freqs-bits-length) 0)

)

"Testing 2.F"
"1 3/5 is expected."
(expected-codeword-length sample-tree)