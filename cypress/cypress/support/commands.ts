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
    omitElementsWithText(textToOmit: string): Chainable<any>
    tryToFindMoreThanZeroOmitting(query: string, textToOmit: string, numTrials: number): Chainable<any>
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

Cypress.Commands.add('omitElementsWithText', { prevSubject: 'element' }, (elements, textToOmit) => {
  let result: JQuery<HTMLElement> = []
  for(let i = 0; i < elements.length; ++i) {
    const elementText = elements[i].innerText
    const elementDoesNotHaveTheText = elementText.indexOf(textToOmit) < 0
    if (elementDoesNotHaveTheText) {
      result.push(elements[i])
    }
    cy.log(`Element with text "${elementText}" kept: ${elementDoesNotHaveTheText}`)
  }
  return cy.wrap(result)
})

Cypress.Commands.add('tryToFindMoreThanZeroOmitting', (query, textToOmit, numTrials) => {
  cy.get(query).omitElementsWithText(textToOmit).should('have.length.gte', 0).then(result => {
    const numFound: number = result.length
    if (numFound === 0) {
      if (numTrials !== 0) {
        cy.wait(200)
        cy.tryToFindMoreThanZeroOmitting(query, textToOmit, numTrials-1)
      }
    } else {
      cy.wrap(numFound).should('equal', 0)
    }
  })
})
