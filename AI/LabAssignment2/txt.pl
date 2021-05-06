go:-
hypothesize(Animal),
write('animal is'),
write(Animal),
undo.

hypothesize(cheetah) :- cheetah, !.
hypothesize(tiger) :- tiger, !. 
hypothesize(giraffe) :- giraffe, !.
hypothesize(zebra) :- zebra, !. 
hypothesize(ostrich) :- ostrich, !.
hypothesize(penguin) :- penguin, !. 
hypothesize(albatross) :- albatross, !. 
hypothesize(unknown).

cheetah :-
	verify(headache),
	verify(runny_nose),
	verify(sneezing),
	verify(sore_throat).

tiger :-
	verify(fever),
	verify(headache),
	verify(chills),
	verify(body_ache).

giraffe :-
	verify(headache),
verify(abdominal_pain),
verify(poor_appetite),
verify(fever).

zebra:-
verify(fever),
verify(runny_nose),
verify(rash),
verify(conjunctivitis).
ostrich :-
verify(fever),
verify(sweating),
verify(headache),
verify(nausea),
verify(vomiting),
verify(diarrhea).
penguin:-
verify(fever),
verify(sweating),
verify(headache),
verify(nausea),
verify(vomiting),
verify(diarrhea).
albatross:-
verify(fever),
verify(sweating),
verify(headache),
verify(nausea),
verify(vomiting),
verify(diarrhea).

/* how to ask questions */
ask(Question) :-
write('Does the animal:'),
write(Question),
write('? '),
read(Response),
nl,
( (Response == yes ; Response == y)
->
assert(yes(Question)) ;
assert(no(Question)), fail).
:- dynamic yes/1,no/1.
/*How to verify something */
verify(S) :-
(yes(S)
->
true ;
(no(S)
->
fail ;
ask(S))).
/* undo all yes/no assertions*/
undo :- retract(yes(_)),fail.
undo :- retract(no(_)),fail.
undo.