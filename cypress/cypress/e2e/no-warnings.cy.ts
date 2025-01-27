describe('Tests of frank-manual config - no warnings', () => {
  xit('Test that there are no alerts in the status page', () => {
    cy.visit('')
    // cy.get('[data-cy-status-alert]').should('have.length', 0)
    cy.tryToFindMoreThanZero('.alert-warning', 10)
  })

  it('Test that there are only alerts about FrankConfig-compatibility', () => {
    cy.visit('')
    cy.tryToFindMoreThanZeroOmitting('.alert-warning', 'FrankConfig-compatibility', 10)
  })
})