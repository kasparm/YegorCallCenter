# Call Center Design
Source: https://github.com/donnemartin/system-design-primer/blob/master/solutions/object_oriented_design/call_center/call_center.ipynb
## Constraints and assumptions
### What levels of employees are in the call center?
        Operator, supervisor, director
### Can we assume operators always get the initial calls?
        Yes
### If there is no available operators or the operator can't handle the call, does the call go to the supervisors?
        Yes
### If there is no available supervisors or the supervisor can't handle the call, does the call go to the directors?
        Yes
### Can we assume the directors can handle all calls?
        Yes
### What happens if nobody can answer the call?
        It gets queued
### Do we need to handle 'VIP' calls where we put someone to the front of the line?
        No
### Can we assume inputs are valid or do we have to validate them?
        Assume they're valid
## Purpose
Yegor Bugayenko wrote a book about opject-oriented programing callend Elegand Objects. Some people call the approach contravertial, some are trying to adapt the concepts from the book and some whould like to propose changes.
This software will implement a call center where people can call in and get issues resolved.

## Design
We will designing this with 4 classes:
- Call
- Employee
  - Operator
  - Supervisor
  - Director
- Caller
- Issue

