(* Higher Order *)

(* Trying things out *)

let succ = function x -> x + 1 ;;
succ 5 ;;
(function x -> x + 1) 5 ;;

let times = function x -> function y -> x*y ;;
times 13 7 ;;
times 13 ;;
let double = times 2 ;;
let double y =  times 2 y ;;
double 10 ;;

let double_fun f x = double (f x) ;;
let floor x = int_of_float(x);;
double_fun floor 2.6 ;;
double_fun (function x -> x*x*x) 12 ;;
let double_floor = double_fun floor ;;
double_floor 12.3 ;;

(* Sums *)
(* Sum of integers to i *)
let sumUpToN n =
  if n < 0 then
    invalid_arg "sumUpToN: Go play elsewhere. I don't like negative vibes."
  else
    let rec sumUpToNAux n = match n with
        0 -> 0
      | n -> n + sumUpToNAux (n-1)
    in sumUpToNAux n ;;

(* Sum of squares *)
let sumSquares n =
  if n < 0 then
    invalid_arg "sumSquares: Go play elsewhere. I don't like negative vibes."
  else
    let rec sumSquaresAux n = match n with
        0 -> 0
      | n -> n*n + sumSquaresAux (n-1)
    in sumSquaresAux n ;;

(* Sum of first integer images by a function *)
let sum f n =
  if n < 0 then
    invalid_arg "sumSquares: Go play elsewhere. I don't like negative vibes."
  else
    let rec sumAux n = match n with
        0 -> f 0
      | n -> f n + sumAux (n-1)
    in sumAux n ;;

(* Loop *)
let loop p f x =
  let rec loopAux p f x = function
      n when p(f x) -> print_int(n) ; f x
    | n -> loopAux p f (f x) (n+1)
  in loopAux p f x 1 ;;

(* Map *)
let rec map f = function
    [] -> []
  | h::t -> (f h)::(map f t);;

(* Iter *)
let rec iter f = function
    [] -> ()
  | h::t -> f h ; iter f t;;

(* Mapi *)
let mapi f l =
  let rec mapi_aux f n = function
      []-> []
     |h::t -> (f n h)::(mapi_aux f (n+1) t)
  in mapi_aux f 0 l;;

let questionMark i h =
  if (i + h) mod 2 = 1 then h else -h ;;

(* Forall *)
let rec for_all p l = match l with
  | [] -> true
  |h::t -> (p h) && for_all p t;;

(* Exists *)
let rec exists p l = match l with
  | [] -> false
  |h::t -> (p h) || exists p t;;

(* HowMany *)

let rec how_many p l = match l with
    [] -> 0
  | h::t -> (if p h then 1 else 0) + how_many p t ;;

let multiple l n =
  let p h = h mod n = 0
  in how_many p l;;

let rec test operator l =
  match l with
    [] | _::[] -> true
    | h::g::t when operator h g -> test operator (g::t)
    | _ -> false ;;

let geo l q =
  let funk h g = g= q*h in
  test funk l;;

let rec firstInstance p l = match l with
    [] -> failwith "firstInstance : There is no such instance"
   | h::t -> if p h then h else firstInstance p t;;
 

let find_place f  l =
  let rec find_placeAux f l n = match l with
      [] -> failwith " find_place: no value found"
    | h::t -> if f h then n
              else find_placeAux f t (n+1)
  in
  find_placeAux f l 0;;

let odd x = x mod 2 = 1;;

let firstodd = find_place odd;;

let rec filter p l = match l with
  |[] -> []
  |h::t when p h -> h::(filter p t)
  |h::t -> filter p t ;;

let partition_reverse l p =
  let rec partition_rec l l1 l2 = match l with
    | [] -> (l1, l2)
    | h::t when p h -> partition_rec t (h::l1) l2
    | h::t -> partition_rec t l1 (h::l2)
  in partition_rec l [] [] ;;

let rec partition l p = match l with
    [] -> ([], [])
  | h::t -> let (l1, l2) = partition t p in
            if p h then (h::l1, l2) else (l1, h::l2) ;;
  
(* exists2 *)

let rec exists2_si p a b =
  match (a, b) with
    ([], []) -> false
  | (_, []) | ([], _) -> failwith "exists2_si: Lists are not of same length and no two elements at same rank satisfying predicate."
  | (h::t, h1::t1) -> p h h1 || exists2_si p t t1;; 

(* Count2 *)

let count2 p a b =
let rec count2Aux p a b n = match (a, b) with
    ([], []) -> n
  | (_, []) | ([], _) -> failwith "count2 : the two list are not of the same size"
  | (h::t, h1::t1) -> if p h h1 then count2Aux p t t1 (n+1)
                      else count2Aux p t t1 n
in
count2Aux p a b 0;; 

let rec count2 p l1 l2 = match (l1, l2) with
  ([], []) -> 0
| (_, []) | ([], _) -> failwith "count2 : the two list are not of the same size"
  | (h::t, h1::t1) -> (if p h h1 then 1 else 0) + count2 p t t1 ;;
  
(* Process List *)

let rec process_list f init =
  function
    [] -> init
  | e::l -> f e (process_list f init l) ;;

let sum l = process_list (+) 0 l;;

let concatenate l =
  process_list (function e -> function call-> e^call) "" l ;;

let append l1 l2 =
  process_list (function e -> function call -> e::call) l2 l1;;


let map f l =
  process_list (function e -> function call -> (f e)::call) [] l;;

let for_all p l =
  process_list (function e -> function call -> p e && call) true l ;;

let rec fold_right f a l = match l with
    [] -> a
   |h::t -> f (fold_right f a t) h ;;

let rec fold_left f a l = match l with
  | [] -> a
  | h::t -> fold_left f (f a h) t;;
