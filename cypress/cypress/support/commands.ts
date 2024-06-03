// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })

declare namespace Cypress {
  interface Chainable<Subject = any> {
    tryToFindMoreThanZero(query: string, numTrials: number)
  }
}

Cypress.Commands.add('tryToFindMoreThanZero', (query, numTrials) => {
  cy.get(query).should('have.length.gte', 0).then(result => {
    const numFound: number = result.length
    if (numFound === 0) {
      if (numTrials !== 0) {
        cy.wait(200)
        cy.tryToFindMoreThanZero(query, numTrials-1)
      }
    } else {
      cy.wrap(numFound).should('equal', 0)
    }
  })
})