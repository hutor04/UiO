(load "prekode3a.rkt")

; Task 1.A. 1.B
(define (memorize-proc proc)
  (let ((table (make-table)))
    (lambda args
      ;  Search for the previously computed value
      (let ((computed-result (lookup args table)))
        ; If value is in table, return it
        (or computed-result
            ;  If there is no such value for the args, calculate and store
            ;  them in table
            (let ((result (apply proc args)))
              (insert! args result table)
              result))))))

(define (memorizer)
  (let ((table (make-table)))
   ; Memorize procedure 
   (define (memorize proc)
     (let ((result (memorize-proc proc)))
          (insert! result proc table)
          result))
    ; Unmemorize procedure
    (define (unmemorize proc)
      (let ((original-proc (lookup proc table)))
          (or original-proc
              proc)))
    ; Dispetcher
    (define (dispatch message proc)
      (cond ((eq? message 'memoize) (memorize proc))
            ((eq? message 'unmemoize) (unmemorize proc))))
    dispatch))
        
       
(define mem (memorizer))

"Testing 1.A and 1.B"
(set! fib (mem 'memoize fib))
(fib 3)
(fib 2)
(fib 4)
(set! fib (mem 'unmemoize fib))
(fib 3)

(set! test-proc (mem 'memoize test-proc))
(test-proc)
(test-proc)
(test-proc 40 41 42 43 44)
(test-proc 40 41 42 43 44)
(test-proc 42 43 44)

; Task 1.C
; It happens because in the definition (define mem-fib (mem 'memoize fib))
; the binding to fib remains unchanged. mem-fib is still using the original fib procedure.
; When we use (set! fib (mem 'memoize fib)), we change the binding of the fib
; as the result the fib procedure that is the body of the procedure is also
; memorized.

; Task 1.D
(define (keyword-helper key args default)
  (define (find-key key args default)
    (cond
      ((null? args) default)
      ((equal? key (car args)) (cadr args))
      (else (find-key key (cddr args) default))))
  
  (if (null? args)
      default
      (find-key key args default)
      )
  )


(define (greet . args)
  (display "Good ")
  (display (keyword-helper 'time args "day"))
  (display " ")
  (display (keyword-helper  'title args "friend"))
  (display "\n")
  )

"Testing Task 1.D"
(greet)
(greet 'time "evening")
(greet 'title "sir" 'time "morning")
(greet 'time "afternoon" 'title "dear")

; Task 2.A

(define (list-to-stream list)
  ; If lis is empty, return an empty stream
  (if (null? list)
      the-empty-stream
      ; Build up the stream from list items
      (cons-stream (car list) (list-to-stream (cdr list)))))


(define (stream-to-list stream . args)
  ; If no counter value is provided initialize counter to -1
  (let ((counter (if (null? args)
                      -1
                     (car args))))
    ; If we consumed the stream or counter is 0, we stop
    (if (or (stream-null? stream) (zero? counter))
        '()
        ; Build up the list
        (cons (stream-car stream)
              (stream-to-list (stream-cdr stream) (- counter 1))))))

"Testing 2.A"
(list-to-stream '(1 2 3 4 5))
(stream-to-list (stream-interval 10 20))
(show-stream nats 15)
(stream-to-list nats 10)

; Task 2.B
(define (find-empty-streams streams)
  (cond ((null? streams) '())
        ((stream-null? (car streams))
         (cons (car streams)
               (find-empty-streams (cdr streams))))
        (else (find-empty-streams (cdr streams)))))

(define (stream-map proc . streams)
  (if (< 0 (length (find-empty-streams streams)))
      the-empty-stream
      (cons-stream
       (apply proc (map stream-car streams))
       (apply stream-map
              (cons proc (map stream-cdr streams))))))

"Testing 2.B"
(define s10 (stream-interval 1 10))
(define s15 (stream-interval 1 15))
"Shortest stream's length is 10, stream-map must return 10 elements"
(length (stream-to-list (stream-map + s10 s15)))
(show-stream  (stream-map + s10 s15 s10))

; Task 2.C
; Potential problem is that stream-memq will not function correctly with
; endless lists, because if an element is not found during the examination
; of the stream the program will be consuming the stream endlessly.

; Task 2.D
(define (remove-duplicates stream)
  ; Returns false, if we've seen the element
  (define (compare-previous element)
    (not (eq? element (stream-car stream)))
    )
  (if (stream-null? stream)
      the-empty-stream
      (cons-stream (stream-car stream)
                   (remove-duplicates
                    (stream-filter compare-previous (stream-cdr stream))))))

"Testing 2.D"
(define dupes (list-to-stream '(5 1 2 3 4 5 1 2 3 4 5)))
"Stream with duplicates"
(show-stream dupes)
"Stream without duplicates"
(show-stream (remove-duplicates dupes))

; Task 2.E
"Task 2.E"
(define (show x)
  (display x)
  (newline)
  x)

(define x (stream-map show (stream-interval 0 10)))
; First get we 0 in output, because the first element of the stream is
; evaluated, the remaining part of the stream is the promise to evaluate.
(stream-ref x 5)
; Now we evaluate five more elements, but the output begins with 1, because
; 0 was already evaluated and sent to output during the previous call.
(stream-ref x 7)
; The bilt-in special form 'delay' is using memorization, as the result
; elements from 0 to 5 inclusive were already evaluated and the result is
; memorized. Thus 'show' outputs only 6 and 7 in addition.

; Task 2.F
(define (mul-streams . args) 
  (apply stream-map * args))

"Testing 2.F"
(define s10 (stream-interval 1 10))
(define s15 (stream-interval 1 15))
(show-stream (mul-streams s10 s15 s10))

; Task 2.G
(define factorials
  (cons-stream 1
               (mul-streams factorials
                            (stream-cdr (integers-starting-from 0)))))
"Testing 2.G"
(stream-ref factorials 5)
(show-stream factorials 6)