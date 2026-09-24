# Advanced Class Relationships

## Previous Activities

[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)

## Existing System Description:

Classes that currently exists in my system:
Class 1: LogisticsCompany, Class 2: LogisticsVehicle

Problems/Limitations in my current system:
The LogisticsVehicle class currently has many attributes that apply to all vehicle types, but no way to distinguish between specialized vehicles (like trucks, vans, or ships). As the system grows, this will lead to either bloated general-purpose classes or repeated code for each vehicle type.


Explanation:
## Inheritance Relationship

Parent: LogisticsVehicle

Child: TransportTruck

Explanation: TransportTruck is a type of LogisticsVehicle because it shares all the general properties of a logistics vehicle (weight, fuel, mileage, vehicle number code) while adding specialized attributes unique to trucks, such as cargo capacity and trailer type. This follows the IS-A principle: a TransportTruck IS-A LogisticsVehicle.


## Inheritance UML

![Inheritance]()

## Composition/Aggregation

Relationship: Composition

Explanation:
    Class containing another object: TransportTruck

    Contained object: Engine

    Why: I chose composition because the engine is a fundamental, inseperable part of TransportTruck. In my system model, a truck cannot function or even meaningfully exist without its engine. The engine is created by the truck itself inside its '__init__()' and is owned exclusively by that truck. If the truck is removed from the system, the engine is removed as well, demonstrating a strong dependency of the part to the whole.

## Advanced UML Diagram

![Advanced UML]()

## Python Implementation

[Source Code]()

## Test Run

![Test]()

## Object Diagram

![Objects]()

## Reflection

Answers: