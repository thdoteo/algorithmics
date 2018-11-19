(* Exercise sheet I *)

let lint = [1;5;3;5;3;1;2;3;464;2;3;4;3;25];;

(* Sum of elements of an int list *)
let rec sum = function
    [] -> 0
  | h::t -> h + sum t ;;

sum lint ;;

(* Count occurences of an element in a list *)
let rec count x = function
    [] -> 0
  | h::t when h = x -> 1 + count x t
  | _::t -> count x t ;;

count 12 lint;;

let rec count_sorted x = function
    [] -> 0 
  | h::t when h > x -> 0
  | h::t when h = x -> 1 + count_sorted x t
  | _::t -> count_sorted x t ;;

let rec search l x =
  match l with
    [] -> false
   | h::t when h = x -> true
   | h::t -> if h > x then false
             else search t x;;

search lint 1 ;;

let nth l n =
  if n < 1 then
    invalid_arg "nth : n must be non-negative"
  else
      let rec nthAux l n r = match l with
      [] -> failwith "nth : n out of range"
     | h::t -> if n = r then
                 h
               else
                 nthAux t n (r+1)
  in
  nthAux l n 1 ;;

let nth l n =
  if n < 1 then
    invalid_arg "nth : n must be non-negative"
  else
      let rec nthAux l n = match (l, n) with
          ([], _) -> failwith "nth : Out of range" 
        | (h::_, 1) -> h
        | (_::t, n) -> nthAux t (n-1)
      in
      nthAux l n ;;

let l = [1;2;3;4;5;6;7;8;9;10;11;12;13;14;15] ;;
nth l 7 ;;

let growing n =
  let rec growingAux x = function
       [] -> true
     | h::t when h >= x -> growingAux h t
     | _::t -> false
  in
  growingAux min_int n;;

let growing n =
  let rec growingAux x = function
       [] -> true
     | h::t when h >= x -> growingAux h t
     | _::t -> false
  in
  if n = [] then
    true
  else
    let h::t = n in growingAux h t;;




let rec growing l = match l with
    [] -> true
  | h::[] -> true
  | h1::h2::_ when h1 > h2 -> false
  | _::t -> growing t ;;

let maximum l =
  let rec maxi l m = match l with
    | [] -> m
    |h::t when h > m -> maxi t h
    |_::t -> maxi t m
  in
  match l with
    [] -> failwith "maximum : This is an empty list, I can't compute its max"
  | h::t -> maxi t h ;;

(* Arithmetic list *)

let arith_list n a1 r =
  if n <= 0 then invalid_arg "n has to be positive"
  else
    let rec arith_listAux n a1 r = match n with
      1 -> [a1]
      | _ -> a1 :: arith_listAux (n-1) (a1+r) r
    in arith_listAux n a1 r ;;

arith_list 12 2 (-2);;


(* Concatenation *)

let rec concatenate l1 l2 = match l1 with
    [] -> l2
  | h::t -> h::(concatenate t l2) ;;

concatenate [1;2;3] [2;3;5] ;;

let del l x =
  if l=[] then
    invalid_arg" the list is empty"
  else
    let rec delAux l x = match l with
     [] |h::t when x < h  -> l
      |h::t when x = h -> t
      |h::t -> h::delAux t x
    in
    delAux l x;;

(* Insertion *)
let rec insertion l x = match l with
  | [] -> x::[]
  | h::t when h >= x -> x::l
  | h::t -> h::(insertion t x);;

(* Reverse *)
let reverse l1 =
  let rec reverseaux l1 l2 =match l1 with
     [] -> l2
    | h::t -> reverseaux t (h::l2)
  in
  reverseaux l1 [] ;;

reverse [1;5;7;658;65;4;1;3221;48;356] ;;

let rec reverse l = match l with
    [] -> []
  | h::t -> (reverse t) @ (h::[]);;

(* Equality *)
let rec equal l1 l2 = match (l1,l2) with
  | ([], [])-> true
  | ( [], _)|( _, []) -> false
  | ( (h1::t1), (h2::t2) ) when h1 = h2 -> equal t1 t2
  | _ -> false;;

(* Shared *)
let rec shared l1 l2=
  match (l1, l2) with
    ([],_)|(_,[])-> []
    |((h1::t1),(h2::t2)) when h1 = h2-> h1::(shared t1 t2)
    |((h1::t1),(h2::t2)) when h1 > h2 -> shared l1 t2
    |((h1::t1), (h2::t2))-> shared t1 l2;;

let rec shared l1 l2=
  match (l1, l2) with
    ([],_)|(_,[])-> []
    |((h1::t1),(h2::t2)) ->
      begin
        if h1 = h2 then
          h1::(shared t1 t2)
        else
          if h1 > h2 then
            shared l1 t2
          else
            shared t1 l2
      end ;;

(* Merge *)
let rec merge (l1, l2) =
  match (l1, l2) with
    ([], l) | (l, []) -> l
    |(h1::t1, h2::t2) ->
      begin
        if h1 = h2 then
          h1::h2::(merge (t1,t2))
        else
          if h1 > h2 then
            h2::(merge (l1, t2))
          else
            h1::(merge (t1, l2))
        end;;
                  
(* Polynomials *)
(* Addition *)
let rec add_poly (p1, p2) = match (p1, p2) with
  |([], a) | (a, []) -> a
  |((c1, d1)::l1, (c2, d2)::l2) ->
    if d1 = d2 then
      if c1 + c2 = 0 then
        add_poly (l1, l2)
      else
        ((c1 + c2), d1)::add_poly(l1, l2)
    else if d1 > d2 then
      (c1, d1)::add_poly(l1, p2)
    else (c2, d2)::add_poly(p1, l2) ;;

(* Multipyling a a monomial with a polynomial *)
let rec mult_poly p m = match p with
    [] -> []
  | (c, d)::t -> let (x, y) = m in (c*x, d+y)::mult_poly t m ;;

(* Multiplication *)
let rec product_poly p1 p2 = match (p1, p2) with
    ([], p) | (p, []) -> []
  | (h::t, _) -> add_poly(mult_poly p2 h, product_poly t p2) ;;

(* Eratosthenes sieve *)
(* Range *)
let range n =
  let rec rangeAux n a = match n with
      1 -> []
    | n -> a::rangeAux (n-1) (a+1)
  in rangeAux n 2 ;;

(* Erasing multiples of p in a list *)
let rec erasemultp l p = match l with
    [] -> []
  | h::t when h mod p = 0 -> erasemultp t p
  | h::t -> h::erasemultp t p ;;

(* Eratosthenes *)
let eratosthenes n =
  if n < 2 then
    failwith "There are no prime numbers smaller than 2"
  else
    let l = range n in
    let rec erAux l = match l with
        [] -> []
      | h::t when h*h > n -> l                
      | h::t -> h::erAux (erasemultp t h)
    in erAux l ;;
