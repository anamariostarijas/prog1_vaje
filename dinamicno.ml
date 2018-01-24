
(* ===== Vaja: Dinamično programiranje  ===== *)
(*let rec dolzina_max_skupnega xs ys =
  match xs, ys with
  | [], _ | _, [] -> 0
  | x :: xs', y :: ys' when x = y ->
    1 + dolzina_max_skupnega xs' ys'
  | _ :: xs', _ :: ys' ->
    max
      (dolzina_max_skupnega xs ys')
      (dolzina_max_skupnega xs' ys)

let rec max_skupno xs ys =
  match xs, ys with
  | [], _ | _, [] -> (0, [])
  | x :: xs', y :: ys' when x = y ->
    let d, zs = max_skupno xs' ys' in
    (d + 1, x :: zs)
  | _ :: xs', _ :: ys' ->
    max
      (max_skupno xs ys')
      (max_skupno xs' ys)

let max_narascajoce xs =
  let rec aux mini xs =
    match mini, xs with
    | _, [] -> (0, [])
    | None, x :: xs'
    | Some mini, x :: xs' when mini <= x ->
        let d, zs = aux x xs' in
        (d + 1, x :: zs)
    | mini, _ :: xs' -> aux mini xs'
  in
  aux None xs*)
  
(* Požrešna miška se nahaja v zgornjem levem kotu šahovnice. Premikati se sme
   samo za eno polje navzdol ali za eno polje na desno in na koncu prispeti v
   desni spodnji kot. Na vsakem polju šahovnice je en sirček. Ti sirčki imajo
   različne (pozitivne) mase. Miška bi se rada kar se da nažrla, zato jo zanima,
   katero pot naj ubere.

   Napišite funkcijo "max_cheese cheese_matrix", ki dobi matriko z
   masami sirčkov in vrne največjo skupno maso, ki jo bo miška požrla, če gre po
   optimalni poti.

   ----------
   # max_cheese cheese_matrix;;
   - : int = 13
   ----------*)

let test_matrix = [| [| 1 ; 2 ; 0 |];
                     [| 2 ; 4 ; 5 |];
                     [| 7 ; 0 ; 1 |]  |]

let max_cheese cheese_matrix = ()

(* Rešujemo problem stolpov, ko smo ga spoznali na predavanjih.
   Imamo štiri različne tipe gradnikov, dva modra in dva rdeča.
   Modri gradniki so višin 2 in 3, rdeči pa višin 1 in 2.

   Napiši funkcijo "alternating_towers height", ki za podano višino "height"
   izpiše število različnih stolpov podane višine, kjer se barva gradnikov
   izmenjuje (rdeč na modrem, moder na rdečem itd.).

   Namig: Uporabi dve pomožni funkciji. Za medsebojno rekurzijo uporabi
          ukaz "and".
   ----------
   # alternating_towers 10;;
   - : int = 35
   ---------- *)
let memoiziraj f =
  let rezultati = Hashtbl.create 512 in
  let mem_f x =
    match Hashtbl.find_opt rezultati x with
    | None ->
        let y = f x in
        Hashtbl.add rezultati x y;
        y
    | Some y -> y
  in
  mem_f
  
let memoiziraj_rec odviti_f =
  let rezultati = Hashtbl.create 512 in
  let rec mem_f x =
    match Hashtbl.find_opt rezultati x with
    | None ->
        let y = odviti_f mem_f x in
        Hashtbl.add rezultati x y;
        y
    | Some y -> y
  in
  mem_f

let memoiziraj_rec2 odviti_f odviti_g =
  let rezultati_f = Hashtbl.create 512
  and rezultati_g = Hashtbl.create 512 in
  let rec mem_f x =
    match Hashtbl.find_opt rezultati_f x with
    | None ->
        let y = odviti_f mem_f mem_g x in
        Hashtbl.add rezultati_f x y;
        y
    | Some y ->
        y
  and mem_g x =
    match Hashtbl.find_opt rezultati_g x with
    | None ->
        let y = odviti_g mem_f mem_g x in
        Hashtbl.add rezultati_g x y;
        y
    | Some y -> y
  in
  (mem_f, mem_g)
  
let rec alternating_towers height = 
	let rec blue = function
		|0 -> 1
		|n when n<0 -> 0
		|n -> red (n-2) + red (n-3)
	and
	    red = function
		|0 -> 1
		|n when n<0 -> 0
		|n -> blue (n-1) + blue (n-2)
	in blue height + red height
		
 