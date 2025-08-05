describe('Tests of frank-manual config - no warnings', () => {
  it('Test that there are no alerts in the status page', () => {
    cy.visit('')
    // cy.get('[data-cy-status-alert]').should('have.length', 0)
    cy.tryToFindMoreThanZero('.alert-warning', 10)
    cy.tryToFindMoreThanZero('.alert-error', 10)
    cy.tryToFindMoreThanZero('.alert-danger', 10)
  })

  it('Test that there are only alerts about FrankConfig-compatibility', () => {
    cy.visit('')
    cy.tryToFindMoreThanZeroOmitting('.alert-warning', 'FrankConfig-compatibility', 10)
    cy.tryToFindMoreThanZero('.alert-error', 10)
    cy.tryToFindMoreThanZero('.alert-danger', 10)
  })
})