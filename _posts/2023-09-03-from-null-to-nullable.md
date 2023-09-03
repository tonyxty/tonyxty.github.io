---
title: From Null to Nullable
series: Why complicated type systems are useful
---

Every java programmer hates `NullPointerException`.  Indeed, any variable[^1] in java can take this special value of `null`, which indicates a lack of value in this variable.  They are like landmines in your code; stomp upon one and boom!  Your program is dead.  Thus, programming in java is like wading through a minefield.  You have to add checks like `if (var != null)` in a lot of places, which is error-prone and cumbersome[^2].

`null` is useful sometimes; we often need to deal with varaibles with no reasonable value in day-to-day coding.  The clever reader will immediately point out that the problem lies in the implicit assumption that any variable *can* be `null`.  As we coders write code, we know some variable will always hold a valid value; but this piece of information is not kept anywhere.  After passing this value around to different functions and assigning new values to it, this piece of information will be lost.  In particular, when returning a value from a function, the caller has no clue whether the return value is nullable without consulting documentation.

But the compiler ought to know!  If we require each nullable variable to be marked with a special annotatation `nullable`, and each use of a nullable variable be prefixed with a nullity check, such runtime exceptions will become compile-time errors, and the code will become easier to write and understand, which is always a good thing.

Much like data types, nullablity defines what value a variable can hold, and what operations we can do with it.  Put more concretely, a nullable varaible of base type `T` obeys three laws:

{:start="0"}
0.  The special value `null` can be assigned to this variable.
1.  Any value of type `T` can be assigned to this variable.
2.  If this variable is not `null`, then a value of type `T` can be extracted from it.

There are various ways to implement such a construction.  There is one important note though: a nullable variable of type `T` behaves fundamentally differently from a variable of type `T`, and therefore should be considered of a different type.  Here is the change of point of view: instead of saying `x` is a nullable variable of type `T`, saying `x` is a variable of type `Nullable<T>` more accurately describes the situation.  This POV, however, requires that the compiler understands the following concept:

> For each type `T`, there is a type `Nullable<T>` whose behavior can be defined in an uniform way.

By uniform I mean the definition does not depend on knowledge of the structure of the type `T`.  "Hey, that's what generics do!"  I heard the readers yell.  Yes, that's generics, which is the ability construct new types from existing types, or "types parameterized by types".  We have successfully established an important proposition:

> In order to eliminate `NullPointerException`, we need generics.

This series of articles will revolve around such ideas, that stronger type system will give us the ability to detect more sophiscated errors at compile-time and, in turn, enable us to write concise and robust code.

[^1]: Well, almost any.  Variables of primitive types can't be null.
[^2]: There are some workarounds, but none of them are satisfactory.
