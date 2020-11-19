; 1.A

(define make-counter
  (lambda ()
    (let ((count 0))
      (lambda ()
        (set! count (+ count 1))
        count)
      )
    )
  )

"Tating 1.A"
(define count 42)
(define c2 (make-counter))
(define c1 (make-counter))
(c1)
(c1)
(c1)
count
(c2)

; 1.B
;                     parameters:
;                     body:...
;                     @=@+----->+-------+
;                      ^        |       +<--+E1
;                      |        +---+---+
;                      |            |
;                      |            |
;                      |            v
;                  +----------------------------+
;                  |   +                        |
;global env +----->+ make-counter:              |
;                  | count:42                   |     +-------+
;                  | c1:                   c2:  +<----+count:0+<--+E3
;                  |  +                     +   |     +---+---+
;                  +------------+---------------+         ^
;                     |         ^           |             |
;                     |         |           |         +---+---+
;                     |     +---+---+       |         |count:1|
;                     |E2+->+count:3|       |         +---+---+
;                     |     +---^---+       |             ^
;                     |         |           |             |
;                     v         |           v             |
;                    @=@+-------+          @=@+-----------+
;                    v                     |
;                    parameters: <---------+         
;                    body:...            


; 2.A
(define (make-stack items)
  (let ((stack items))
    ; Pop item from stack
    (define (pop!)
      (if (not (null? stack))
          (set! stack (cdr stack))
          )
      )

    ; Push items to stack
    (define (push! args)
      (set! stack (append (reverse args) stack))
      )

    ; Dispatcher
    (define (dispatch message . args)
      (cond 
        ((eq? message 'pop!) (pop!))
        ((eq? message 'push!) (push! args))
        ((eq? message 'stack) stack)
        ))
    dispatch))

"Testing 2.A"
(define s1 (make-stack (list 'foo 'bar)))
(define s2 (make-stack '()))
(s1 'pop!)
(s1 'stack)
(s2 'pop!)
(s2 'push! 1 2 3 4)
(s2 'stack)
(s1 'push! 'bah)
(s1 'push! 'zap 'zip 'baz)
(s1 'stack)

; 2.B
(define (pop! stack)
  (stack 'pop!))

(define (stack stack)
  (stack 'stack))

(define (push! stack . args)
  (apply stack 'push! args))

"Testing 2.B"
(pop! s1)
(stack s1)
(push! s1 'foo 'faa)
(stack s1)

; 3.A
;      +------+------+     +------+------+     +------+------+     +------+------+    +------+------+
;      |      |      |     |      |      |     |      |      |     |      |      |    |      |     x|
;+---->+  +   |  +-------->+  +   |  +-------->+  +   |  +-------->+  +   |  +------->+  +   |   x  |
;      |  |   |      |     |  |   |      |     |  |   |      |     |  |   |      |    |  |   |x     |
;      +------+------+     +------+------+     +------+------+     +------+------+    +-------------+
;         |                   |                   |                   |                  |
;         v                   v                   v                   v                  v
;         A                   B                   C                   D                  E
;
;============================================================================================================
;                              +--------------------------------------------+
;                              |                                            |
;                              |                                            |
;                              v                                            |
;      +------+------+     +---+--+------+    +------+------+    +------+------+
;      |      |      |     |      |      |    |      |      |    |      |   |  |
;+---->+  +   |  +-------->+  +   |  +------->+  +   |  +------->+  +   |   +  |
;      |  |   |      |     |  |   |      |    |  |   |      |    |  |   |      |
;      +------+------+     +------+------+    +------+------+    +------+------+
;         |                   |                  |                  |
;         v                   v                  v                  v
;         A                   B                  C                  D

; CDR part of CDDDR of original bar list is now pointing to the CDR part of the
; bar

; 3.B
;      +------+------+     +------+------+     +------+------+
;      |      |      |     |      |      |     |      |     x|
;+---->+  +   |  +-------->+  +   |  +-------->+  +   |   x  |
;      |  |   |      |     |  |   |      |     |  |   |x     |
;      +------+------+     +------+------+     +-------------+
;         |                   |                   |
;         v                   v                   v
;         'bring              'a                  'towel
;
;=============================================================================
;
;         +-------------------+
;         |                   v
;      +------+------+     +--+---+------+     +------+------+
;      |  |   |      |     |      |      |     |      |     x|
;+---->+  +   |  +-------->+  +   |  +-------->+  +   |   x  |
;      |      |      |     |  |   |      |     |  |   |x     |
;      +------+------+     +------+------+     +-------------+
;                             |                   |
;                             v                   v
;                             'a                  'towel
;
; Aften the second call of set-car!, car of bah, and cdr of bah refer to the
; same object. Tha can be also tested with (eq? (car bah) (cdr bah))

; 3.C
; Based on https://en.wikipedia.org/wiki/Cycle_detection (Floyd's Algo)
(define bar (list 'a 'b 'c 'd 'e))
(set-cdr! (cdddr bar) (cdr bar))

(define bah (list 'bring 'a 'towel))
(set-car! bah (cdr bah))


(define (cycle? items)
  (define (cycle-iter turtle rabbit)
    (cond
      ; Can rabbit run?
      ((or (null? rabbit) (null? (cdr rabbit))) #f)
      ; Found match
      ((eq? turtle rabbit) #t)
      ; Turtle 1 step, Rabbit 2 steps
      (else (cycle-iter (cdr turtle) (cddr rabbit)))
      )
    )
  (cond
    ((null? items) #f)
    (else (cycle-iter items (cdr items)))))

"Testing 3.C"
(cycle? '(hey ho))
(cycle? '(la la la))
(cycle? bah)
(cycle? bar)

; 3.D
; Based on https://docs.racket-lang.org/guide/pairs.html
; A list is a combination of pairs that creates a linked list.
; A list is either the empty list null, or it is a pair whose first element is
; a list element and whose second element is a list.
; While a pair joins two arbitrary values.
; 'bar' is a pair because its second element is not a list. And the second
; element, in its turn, is not a list because its last element is not pointing
; to an empty list.

; 3.E
(define (make-ring items)
  (let ((ring items))
    ; Top Element
    (define (top)
      (if (not (null? ring))
          (car ring)
          )
      )

    ; Left Rotate
    (define (left-rotate!)
      (if (not (null? ring))
          (let ((first-element (list (car ring))))
            (set! ring (append (cdr ring) first-element))
            )
          )
      )

    ; Right Rotate
    ; Last Element
    (define (last-element items)
      (cond ((null? (cdr items)) (car items))
            (else (last-element (cdr items)))
            )
      )

    ; Remove Last Element
    (define (remove-last items)
    (if (null? (cdr items))
        '()
        (cons (car items) (remove-last (cdr items)))))

     (define (right-rotate!)
       (if (not (null? ring))
           (let* ((last (list (last-element ring)))
                 (rest (remove-last ring)))
             (set! ring (append last rest))
            )
          ))
       
    ; Insert Item
    (define (insert! item)
      (set! ring (append item ring)))

    ; Delete Item
    (define (delete!)
      (set! ring (cdr ring)))

    ; Dispatcher
    (define (dispatch message . args)
      (cond 
        ((eq? message 'top) (top))
        ((eq? message 'left-rotate!) (left-rotate!))
        ((eq? message 'right-rotate!) (right-rotate!))
        ((eq? message 'insert!) (insert! args))
        ((eq? message 'delete!) (delete!))
        ((eq? message 'ring) ring)
        ))
    dispatch))

; Interface
(define (top ring)
  (ring 'top))

(define (left-rotate! ring)
  (ring 'left-rotate!)
  (ring 'top))

(define (right-rotate! ring)
  (ring 'right-rotate!)
  (ring 'top))

(define (insert! ring element)
  (ring 'insert! element)
  (ring 'top))

(define (delete! ring)
  (ring 'delete!)
  (ring 'top))

"Testing 3.E"
(define r1 (make-ring '(1 2 3 4)))
(define r2 (make-ring '(a b c d)))
(top r1)
(top r2)
(right-rotate! r1)
(left-rotate! r1)
(left-rotate! r1)
(delete! r1)
(left-rotate! r1)
(left-rotate! r1)
(left-rotate! r1)
(insert! r2 'x)
(right-rotate! r2)
(left-rotate! r2)
(left-rotate! r2)
(top r1)

; Task 3.F
; The implementation is not very effecient, since I am updating the ring
; via copies. Right-rotate! makes two passes over the ring to find the last
; element and to remove the last element from the ring O(2N), N - ring size.
; This may be problematic with the rings og bigsize.
; Potentially, these issues can be addressed by having pointers to the first,
; last-but-one, and last elements of the ring or by using lists with circular
; reference.
