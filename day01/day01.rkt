#lang racket

(let ([freq_changes (file->list "input.txt")])
  (println (apply + freq_changes))
  
  (println (for/fold ([already_seen (set)]
                      [freq 0]
                      #:result freq)
                     ([num (in-cycle freq_changes)]
                      #:break (set-member? already_seen freq))
             (let ([next (+ freq num)])
               (values (set-add already_seen freq) next)))))
