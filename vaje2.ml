(* ===== Exercise 2: Functional Programming  ===== *)

(*Hint: Write a function for reversing lists.*)

(* The function "repeat x n" returns a list with n repetitions of x.
 For unsuitable n it returns an empty list.
 ----------
 # repeat "A" 5;;
 - : string list = ["A"; "A"; "A"; "A"; "A"]
 # repeat "A" (-2);;
 - : string list = []
 ---------- *)
let rec reverse = function
    | hd :: tl -> reverse tl @ [hd]
	| [] -> []

	
let rec repeat x n = 
	if n<=0 then [] else match n with
		|1 -> [x]
		|2 ->[x;x]
		|n -> [x]@(repeat x (n-1))
		
let rec repeat2 x n = 
	if n=0
	then []
	else 
		let recursive_result = repeat x (n-1) in
		x :: recursive_result
	
(* The function "range n" returns a list of all non-negative integers up to
 (including) n. For unsuitable n it returns an empty list.
 The function is tail recursive..
 ----------
 # range 10;;
 - : int list = [0; 1; 2; 3; 4; 5; 6; 7; 8; 9; 10]
 ---------- *)

let range_not_tailrec n = 
	let rec range_from m = 
		if m> n
		then []
		else m::(range_from (m+1))
		in range_from 0
		
let range n = 
	let rec range_down n acc = (*nosi s seboj delni rezultat*)
		if n<=0
		then acc
		else range_down (n-1) (n::acc)
	in range_down n []
	
(* The function "map f l" accepts a list l = [l0; l1; l2; ...] and a function f
 and returns the list [f l0; f l1; f l2; ...].
 ----------
 # let plus_two = (+)2 in
   map plus_two [0; 1; 2; 3; 4];;
 - : int list = [2; 3; 4; 5; 6]
 ---------- *)

let rec map f l =
	match l with
	|[] -> []
	|x::xs -> (f x) :: (map f xs) 
	
let rec map_rec f l =
	match l with
	|[] -> []
	|x::xs -> let res_rec = map_rec f xs in
	(f x) :: res_rec 
	

(* The function "map_tlrec" is the tail recursive version of map.
 ----------
 # let plus_two = (fun x -> x+2) in
   map_tlrec plus_two [0; 1; 2; 3; 4];;
 - : int list = [2; 3; 4; 5; 6]
 ---------- *)

	
let map_tlrec f l =
  let rec map_aux l res_rev =
    match l with
    | [] -> reverse res_rev
    | x::xs -> map_aux xs (f x :: res_rev)
  in
  map_aux l []

	
(* The function "mapi f l" accepts a list l = [l0; l1; l2; ...] and a function f
 and returns the list [f 0 l0; f 1 l1; f 2 l2; ...].
 ----------
 # mapi (+) [0; 0; 0; 2; 2; 2];;
 - : int list = [0; 1; 2; 5; 6; 7]
 ---------- *)

let rec mapi f l = 
	let rec mapping l acc i =
	match l with
	|[] -> reverse acc
	|x::xs -> mapping xs ((f i x):: acc) (i+1)
	in mapping l [] 0 	
	
		
		
(* The function "zip l1 l2" accepts lists l1 = [l1_0; l1_1; l1_2; ...] and
 l2 = [l2_0; l2_1; l2_2; ...] and returns the list [(l1_0,l2_0); (l1_1,l2_1); ...].
 If the lenght of lists l1 and l2 doesn't match it fails.
 ----------
 # zip [1; 1; 1; 1] [0; 1; 2; 3];;
 - : (int * int) list = [(1, 0); (1, 1); (1, 2); (1, 3)]
 # zip [1; 1; 1; 1] [1; 2; 3; 4; 5];;
 Exception: Failure "Different lengths.".
 ---------- *)

let rec zip l1 l2 = 
	match (l1, l2) with	
	|(x::xs, hd::tl) -> [(x, hd)]@zip xs tl
	|([], []) -> []
	|([], l2) -> failwith "Different lengths."
	|(l1,[]) -> failwith "Different lengths."
	

	(* The function "zip_enum_tlrec l1 l2" accepts lists l1 = [l1_0; l1_1; l1_2; ...] 
 and l2 = [l2_0; l2_1; l2_2; ...] and returns [(0, l1_0, l2_0); (1, l1_1, l2_1); ...].
 The function is tail recursive..
 If the lenght of lists l1 and l2 doesn't match it fails.
 ----------
 # zip_enum_tlrec ["a"; "b"; "c"; "d"] [7; 3; 4; 2];;
 - : (int * string * int) list = [(0, "a", 7); (1, "b", 3); (2, "c", 4); (3, "d", 2)]
 ---------- *)

let zip_enum_tlrec l1 l2 = 
	let rec ziping l1 l2 acc i =
	match (l1, l2) with
	|([],[]) -> reverse acc
	|([], _)|(_, []) -> failwith "Different lengths."
	|(x::xs, hd::tl) -> ziping xs tl ([(i, x, hd)]@acc) (i+1)
	in ziping l1 l2 [] 0

(* The function "unzip l" accepts a list l = [(a0, b0); (a1, b2); ...]
 and returns the pair ([a0; a1; ...], [b0; b1; ...]).
 ----------
 # unzip [(0,"a"); (1,"b"); (2,"c")];;
 - : int list * string list = ([0; 1; 2], ["a"; "b"; "c"])
 ---------- *)

let rec unzip l = 
	match l with 
	|[] -> ([], [])
	|(x,y)::xs -> let (l1, l2) = unzip xs in
	(x::l1, y::l2)
	
(* The function "unzip_tlrec l" is the tail recursive version of unzip.
 ----------
 # unzip_tlrec [(0,"a"); (1,"b"); (2,"c")];;
 - : int list * string list = ([0; 1; 2], ["a"; "b"; "c"])
 ---------- *)

let unzip_tlrec l = 
	let rec unziping l l1 l2 =
	match l with
	|[] -> (reverse l1, reverse l2)
	|(x,y)::xs -> unziping xs (x::l1) (y::l2)
	in 
	unziping l [] []

(* The function "fold_left_no_acc f l" accepts a list l = [l0; l1; l2; ...; ln] and function f
 and returns the value of f(... (f (f (f l0 l1) l2) l3) ... ln).
 If the list has less than two elements it fails.
 ----------
 # fold_left_no_acc (^) ["F"; "I"; "C"; "U"; "S"];;
 - : string = "FICUS"
 ---------- *)

let rec fold_left_no_acc f l = 
	match l with
	|[] | _::[] -> failwith "The list is too short."
	|x::y::[] -> f x y
	|x::hd::tl -> fold_left_no_acc f ((f x hd) :: tl)
	
(* The function "apply_sequence f x n" returns the list of repeated applications 
 of the function f on x, [x; f x; f (f x); ...; f applied n times on x].
 The function is tail recursive.
 ----------
 # apply_sequence (fun x -> x*x) 2 5;;
 - : int list = [2; 4; 16; 256; 65536; 4294967296]
 # apply_sequence (fun x -> x*x) 2 (-5);;
 - : int list = []
 ---------- *)

let apply_sequence f x n = 
	let rec applying f x acc n =
	if n<0 then reverse acc else
	applying f (f x) (x::acc) (n-1) in
	applying f x [] n

(* The function "filter f l" returns the list of elements for which 
 (f x) equals true.
 ----------
 # filter ((<)3) [0; 1; 2; 3; 4; 5];;
 - : int list = [4; 5]
 ---------- *)

let rec filter f l = 
	match l with
	|[] -> []
	|x::xs -> if f x then x::filter f xs else
	filter f xs

(* The function "exists f l" checks if there exists an element of the list l
 for which the function f returns true, otherwise it returns false.
 The function is tail recursive.
 ----------
 # exists ((<)3) [0; 1; 2; 3; 4; 5];;
 - : bool = true
 # exists ((<)8) [0; 1; 2; 3; 4; 5];;
 - : bool = false
 ---------- *)

let rec exists f l = 
	match l with
	|[] -> false
	|x::xs -> f x || exists f xs
	

(* The function "first f none_value l" returns the first element of the list l
 for which f returns true. If such an element does not exist it returns none_value.
 The function is tail recursive.
 ----------
 # first ((<)3) 0 [1; 1; 2; 3; 5; 8];;
 - : int = 5
 # first ((<)8) 0 [1; 1; 2; 3; 5; 8];;
 - : int = 0
 ---------- *)

let rec first f none_value l = 
	match l with
	|[] -> none_value
	|x::xs -> if f x then x else first f none_value xs
  
(* The northerners are attacking Middlebirch. As the archwizard you know the sequence
 of spells needed to protect Middlebirch. The sequence of spells is written as a list
 [("name1", value1); ("name2", value2); ...].
 At your disposal is a band of wizards, who are represented as a list
 [("name1", ability1); ("name2", ability2); ...].
 A wizard can cast the sequence of spells only if his ability is greater or equal to
 the combined value of all spells in the sequence.

 The function "able_protectors spells wizards" returns a list of names of all the
 wizards able to protect Middlebirch on their own.

 The function "fails_on spells wizards" returns a list of pairs (wizard, failed spell),
 where the failed spell is the first spell in the sequence for which the wizard has 
 insufficient ability. The ability to cast all spells is represented as an empty string 
 for the failed spell.
 
 Hint: A good wizard uses his knowledge and experiences gained during his studies.
 
 ----------
 # let spells = [("Protect",51); ("Renounce", 17); ("Blaze", 420); ("Banish",103)] in
   let wizards = [("Merlin", 1832); ("Frodo", 53); ("Atijam", 1337);
  ("Mr Duck", 7); ("Kylo Ren", 589); ("Snoop Dogg", 123)] in
   able_protectors spells wizards;;
 - : string list = ["Merlin"; "Atijam"]
 ----------
 # let spells = [("Protect",51); ("Renounce", 17); ("Blaze", 420); ("Banish",103)] in
   let wizards = [("Merlin", 1832); ("Frodo", 53); ("Atijam", 1337);
  ("Mr Duck", 7); ("Kylo Ren", 589); ("Snoop Dogg", 123)] in
   fails_on spells wizards;;
 - : (string * string) list = [("Merlin", ""); ("Frodo", "Renounce"); ("Atijam", "");
  ("Mr Duck", "Protect"); ("Kylo Ren", "Banish"); ("Snoop Dogg", "Blaze")]
 ----------*)

let able_protectors spells wizards = ()

let fails_on spells wizards = ()
